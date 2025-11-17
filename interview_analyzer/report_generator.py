"""
Report Generator Module
Creates structured reports and visualizations
"""
from typing import Dict, List
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import os

class ReportGenerator:
    def __init__(self, output_dir: str = "outputs"):
        """
        Initialize report generator
        
        Args:
            output_dir: Directory to save reports
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def generate_report_data(self, analysis: Dict, sentiment_data: List[Dict] = None) -> Dict:
        """
        Generate comprehensive report data structure
        
        Args:
            analysis: AI analysis results
            sentiment_data: Optional sentiment trend data
        
        Returns:
            Structured report dictionary
        """
        report = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "overall_summary": analysis.get("overall_summary", ""),
            "participants": analysis.get("participants", {}),
            "sentiment_trend": analysis.get("sentiment_trend", []),
            "topics": analysis.get("topics_discussed", []),
            "keywords": analysis.get("keywords", []),
            "assessment": analysis.get("overall_assessment", {}),
            "detailed_feedback": analysis.get("detailed_feedback", {}),
            "raw_transcript": analysis.get("raw_transcript", "")
        }
        
        # Enhance with sentiment data if provided
        if sentiment_data:
            report["sentiment_trend"] = sentiment_data
        
        return report
    
    def create_sentiment_chart(self, sentiment_trend: List[Dict]) -> go.Figure:
        """
        Create sentiment trend visualization
        
        Args:
            sentiment_trend: List of sentiment data points
        
        Returns:
            Plotly figure
        """
        if not sentiment_trend:
            # Create empty chart
            fig = go.Figure()
            fig.add_annotation(
                text="No sentiment data available",
                xref="paper", yref="paper",
                x=0.5, y=0.5, showarrow=False
            )
            return fig
        
        # Prepare data
        segments = [s.get("segment", f"Segment {i+1}") for i, s in enumerate(sentiment_trend)]
        sentiments = [s.get("sentiment", "Neutral") for s in sentiment_trend]
        confidence = [s.get("confidence", 0.5) for s in sentiment_trend]
        
        # Map sentiments to numeric values for visualization
        sentiment_map = {"Positive": 1, "Neutral": 0, "Negative": -1, "Confident": 0.8, "Nervous": -0.5}
        sentiment_values = [sentiment_map.get(s, 0) for s in sentiments]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=list(range(len(segments))),
            y=sentiment_values,
            mode='lines+markers',
            name='Sentiment',
            line=dict(color='#1f77b4', width=3),
            marker=dict(size=10),
            text=sentiments,
            hovertemplate='<b>%{text}</b><br>Confidence: %{customdata:.2f}<extra></extra>',
            customdata=confidence
        ))
        
        fig.update_layout(
            title="Sentiment Trend Over Time",
            xaxis_title="Conversation Progress",
            yaxis_title="Sentiment Score",
            xaxis=dict(tickmode='array', tickvals=list(range(len(segments))), ticktext=segments),
            yaxis=dict(tickmode='array', tickvals=[-1, 0, 1], ticktext=["Negative", "Neutral", "Positive"]),
            hovermode='closest',
            template='plotly_white',
            height=400
        )
        
        return fig
    
    def create_confidence_chart(self, participants: Dict) -> go.Figure:
        """
        Create confidence score comparison chart
        
        Args:
            participants: Dictionary of participant data
        
        Returns:
            Plotly figure
        """
        if not participants:
            fig = go.Figure()
            fig.add_annotation(
                text="No participant data available",
                xref="paper", yref="paper",
                x=0.5, y=0.5, showarrow=False
            )
            return fig
        
        names = []
        confidence_scores = []
        clarity_scores = []
        empathy_scores = []
        
        for speaker_id, data in participants.items():
            names.append(data.get("name", speaker_id))
            confidence_scores.append(data.get("confidence_score", 0))
            clarity_scores.append(data.get("clarity_score", 0))
            empathy_scores.append(data.get("empathy_score", 0))
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            name='Confidence',
            x=names,
            y=confidence_scores,
            marker_color='#2ecc71'
        ))
        
        fig.add_trace(go.Bar(
            name='Clarity',
            x=names,
            y=clarity_scores,
            marker_color='#3498db'
        ))
        
        fig.add_trace(go.Bar(
            name='Empathy',
            x=names,
            y=empathy_scores,
            marker_color='#9b59b6'
        ))
        
        fig.update_layout(
            title="Communication Metrics by Participant",
            xaxis_title="Participant",
            yaxis_title="Score (0.0 - 1.0)",
            barmode='group',
            template='plotly_white',
            height=400,
            yaxis=dict(range=[0, 1])
        )
        
        return fig
    
    def create_radar_chart(self, participant_data: Dict) -> go.Figure:
        """
        Create radar/spider chart for participant metrics
        
        Args:
            participant_data: Single participant's analysis data
        
        Returns:
            Plotly figure
        """
        categories = ['Confidence', 'Clarity', 'Empathy', 'Engagement', 'Communication']
        values = [
            participant_data.get("confidence_score", 0),
            participant_data.get("clarity_score", 0),
            participant_data.get("empathy_score", 0),
            participant_data.get("engagement_score", 0),
            (participant_data.get("confidence_score", 0) + 
             participant_data.get("clarity_score", 0)) / 2
        ]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name=participant_data.get("name", "Participant"),
            line_color='#e74c3c'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 1]
                )),
            showlegend=True,
            title="Communication Skills Radar",
            template='plotly_white',
            height=400
        )
        
        return fig
