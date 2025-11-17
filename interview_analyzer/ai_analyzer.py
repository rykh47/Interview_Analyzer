"""
AI Analysis Module using Google Gemini
Performs sentiment, tone, empathy, and clarity analysis
"""
import google.generativeai as genai
from typing import Dict, List, Optional
import json
import re
from .config import GEMINI_API_KEY, SENTIMENT_CATEGORIES, EMOTION_CATEGORIES

class AIAnalyzer:
    def __init__(self, api_key: str = None):
        """
        Initialize Gemini API client
        
        Args:
            api_key: Google Gemini API key
        """
        self.api_key = api_key or GEMINI_API_KEY
        if not self.api_key:
            raise ValueError("Gemini API key is required. Set GOOGLE_GEMINI_API_KEY in .env file")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-pro')
    
    def analyze_conversation(
        self,
        transcript: str,
        domain: str = "General",
        round_type: str = "General",
        feedback_tone: str = "Professional"
    ) -> Dict:
        """
        Comprehensive analysis of interview/conversation transcript
        
        Args:
            transcript: Full conversation transcript
            domain: Domain context (Tech, HR, etc.)
            round_type: Type of interview round
            feedback_tone: Tone for feedback (Professional, Encouraging, Critical)
        
        Returns:
            Dictionary with comprehensive analysis
        """
        prompt = self._build_analysis_prompt(transcript, domain, round_type, feedback_tone)
        
        try:
            response = self.model.generate_content(prompt)
            analysis_text = response.text
            
            # Parse the structured response
            analysis = self._parse_analysis_response(analysis_text, transcript)
            return analysis
        except Exception as e:
            raise Exception(f"Error in AI analysis: {str(e)}")
    
    def _build_analysis_prompt(
        self,
        transcript: str,
        domain: str,
        round_type: str,
        feedback_tone: str
    ) -> str:
        """Build comprehensive analysis prompt for Gemini"""
        
        tone_instructions = {
            "Professional": "Provide professional, objective feedback with constructive suggestions.",
            "Encouraging": "Provide warm, encouraging feedback that highlights strengths while gently suggesting improvements.",
            "Critical": "Provide detailed, critical analysis focusing on areas that need significant improvement."
        }
        
        tone_instruction = tone_instructions.get(feedback_tone, tone_instructions["Professional"])
        
        prompt = f"""You are an expert AI Interview Analyzer and mentor. Analyze the following interview/group discussion transcript and provide comprehensive insights.

DOMAIN: {domain}
ROUND TYPE: {round_type}
FEEDBACK TONE: {tone_instruction}

TRANSCRIPT:
{transcript}

Please provide a detailed analysis in the following JSON format (respond ONLY with valid JSON, no markdown):

{{
    "overall_summary": "Brief summary of the entire conversation",
    "participants": {{
        "speaker_1": {{
            "name": "Speaker name or identifier",
            "sentiment": "Overall sentiment (Positive/Negative/Neutral)",
            "tone": "Primary tone (Confident/Nervous/Calm/Enthusiastic/etc.)",
            "confidence_score": 0.0-1.0,
            "clarity_score": 0.0-1.0,
            "empathy_score": 0.0-1.0,
            "engagement_score": 0.0-1.0,
            "key_points": ["point1", "point2", "point3"],
            "strengths": ["strength1", "strength2"],
            "improvements": ["improvement1", "improvement2", "improvement3"],
            "filler_words_count": 0,
            "speaking_pace": "Fast/Moderate/Slow",
            "communication_quality": "Excellent/Good/Average/Needs Improvement"
        }}
    }},
    "sentiment_trend": [
        {{"segment": "First 25%", "sentiment": "Positive", "confidence": 0.8}},
        {{"segment": "Second 25%", "sentiment": "Neutral", "confidence": 0.6}},
        {{"segment": "Third 25%", "sentiment": "Positive", "confidence": 0.7}},
        {{"segment": "Final 25%", "sentiment": "Positive", "confidence": 0.9}}
    ],
    "topics_discussed": ["topic1", "topic2", "topic3"],
    "keywords": ["keyword1", "keyword2", "keyword3"],
    "overall_assessment": {{
        "communication_quality": "Overall assessment",
        "strengths": ["strength1", "strength2"],
        "critical_improvements": ["improvement1", "improvement2"],
        "recommendation": "Overall recommendation for the candidate"
    }},
    "detailed_feedback": {{
        "structure": "Feedback on answer structure",
        "conciseness": "Feedback on conciseness",
        "technical_depth": "Feedback on technical knowledge (if applicable)",
        "interpersonal_skills": "Feedback on interpersonal and communication skills"
    }}
}}

IMPORTANT:
- Analyze each participant separately if multiple speakers are present
- Provide specific, actionable feedback
- Score all metrics on a 0.0-1.0 scale
- Identify filler words (um, uh, like, you know, etc.)
- Assess speaking pace and clarity
- Be specific about improvements needed
- Consider the domain context ({domain}) in your analysis
"""
        return prompt
    
    def _parse_analysis_response(self, response_text: str, transcript: str) -> Dict:
        """Parse Gemini response and extract structured data"""
        try:
            # Try to extract JSON from response
            # Remove markdown code blocks if present
            cleaned_text = response_text.strip()
            if "```json" in cleaned_text:
                cleaned_text = cleaned_text.split("```json")[1].split("```")[0].strip()
            elif "```" in cleaned_text:
                cleaned_text = cleaned_text.split("```")[1].split("```")[0].strip()
            
            # Parse JSON
            analysis = json.loads(cleaned_text)
            
            # Add raw transcript for reference
            analysis["raw_transcript"] = transcript
            
            return analysis
        except json.JSONDecodeError:
            # Fallback: try to extract key information using regex
            return self._fallback_parse(response_text, transcript)
    
    def _fallback_parse(self, response_text: str, transcript: str) -> Dict:
        """Fallback parser if JSON parsing fails"""
        # Extract key information using pattern matching
        analysis = {
            "overall_summary": self._extract_section(response_text, "summary", "overall"),
            "participants": {},
            "sentiment_trend": [],
            "topics_discussed": [],
            "keywords": [],
            "overall_assessment": {},
            "detailed_feedback": {},
            "raw_transcript": transcript
        }
        
        # Try to extract participant info
        # This is a simplified fallback - ideally JSON parsing should work
        return analysis
    
    def _extract_section(self, text: str, *keywords: str) -> str:
        """Extract a section from text based on keywords"""
        for keyword in keywords:
            pattern = rf"{keyword}[:\-]?\s*(.+?)(?:\n\n|\Z)"
            match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()
        return "Analysis not available"
    
    def extract_keywords(self, text: str, top_n: int = 10) -> List[str]:
        """Extract top keywords from transcript"""
        prompt = f"""Extract the top {top_n} most important keywords or key phrases from the following text. 
        Return only a comma-separated list of keywords, no explanations.
        
        Text: {text[:2000]}
        
        Keywords:"""
        
        try:
            response = self.model.generate_content(prompt)
            keywords = [k.strip() for k in response.text.split(",")]
            return keywords[:top_n]
        except:
            return []
