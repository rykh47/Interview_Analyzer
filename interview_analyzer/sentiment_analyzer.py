"""
Sentiment Analysis Module
Uses VADER and additional heuristics for sentiment analysis
"""
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from typing import Dict, List
import re

class SentimentAnalyzer:
    def __init__(self):
        """Initialize VADER sentiment analyzer"""
        self.analyzer = SentimentIntensityAnalyzer()
    
    def analyze_sentiment(self, text: str) -> Dict:
        """
        Analyze sentiment of text
        
        Returns:
            Dictionary with sentiment scores and classification
        """
        scores = self.analyzer.polarity_scores(text)
        
        # Classify sentiment
        if scores['compound'] >= 0.05:
            sentiment = "Positive"
        elif scores['compound'] <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        
        return {
            "sentiment": sentiment,
            "compound": scores['compound'],
            "positive": scores['pos'],
            "neutral": scores['neu'],
            "negative": scores['neg']
        }
    
    def analyze_segments(self, segments: List[Dict]) -> List[Dict]:
        """
        Analyze sentiment for each segment of conversation
        
        Args:
            segments: List of conversation segments with 'text' field
        
        Returns:
            List of segments with added sentiment analysis
        """
        analyzed_segments = []
        for segment in segments:
            text = segment.get('text', '')
            sentiment = self.analyze_sentiment(text)
            
            analyzed_segment = {
                **segment,
                "sentiment": sentiment["sentiment"],
                "sentiment_score": sentiment["compound"],
                "confidence": sentiment["compound"]
            }
            analyzed_segments.append(analyzed_segment)
        
        return analyzed_segments
    
    def count_filler_words(self, text: str) -> int:
        """
        Count filler words in text
        
        Common fillers: um, uh, like, you know, actually, basically, etc.
        """
        filler_patterns = [
            r'\bum\b', r'\buh\b',
            r'\buh\b',
            r'\blike\b',
            r'\byou know\b',
            r'\bactually\b',
            r'\bbasically\b',
            r'\bwell\b',
            r'\bso\b',
            r'\bkind of\b',
            r'\bsort of\b',
            r'\bI mean\b'
        ]
        
        count = 0
        text_lower = text.lower()
        for pattern in filler_patterns:
            matches = re.findall(pattern, text_lower)
            count += len(matches)
        
        return count
    
    def calculate_speaking_pace(self, text: str, duration_seconds: float = None) -> str:
        """
        Calculate speaking pace
        
        Args:
            text: Spoken text
            duration_seconds: Duration of speech in seconds
        
        Returns:
            Pace classification: "Fast", "Moderate", or "Slow"
        """
        if not duration_seconds:
            # Estimate: average speaking rate is 150-160 words per minute
            word_count = len(text.split())
            estimated_duration = word_count / 2.5  # words per second
            duration_seconds = estimated_duration
        
        word_count = len(text.split())
        words_per_minute = (word_count / duration_seconds) * 60 if duration_seconds > 0 else 0
        
        if words_per_minute > 180:
            return "Fast"
        elif words_per_minute < 120:
            return "Slow"
        else:
            return "Moderate"
