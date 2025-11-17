"""
PDF Report Generator
Creates downloadable PDF reports for interview analysis
"""
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from typing import Dict
import os
from datetime import datetime

class PDFGenerator:
    def __init__(self, output_dir: str = "outputs"):
        """
        Initialize PDF generator
        
        Args:
            output_dir: Directory to save PDFs
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()
    
    def _setup_custom_styles(self):
        """Setup custom paragraph styles"""
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#2c3e50'),
            spaceAfter=30,
            alignment=TA_CENTER
        ))
        
        self.styles.add(ParagraphStyle(
            name='SectionHeader',
            parent=self.styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#34495e'),
            spaceAfter=12,
            spaceBefore=12
        ))
        
        self.styles.add(ParagraphStyle(
            name='BodyText',
            parent=self.styles['Normal'],
            fontSize=11,
            leading=14,
            alignment=TA_JUSTIFY
        ))
    
    def generate_pdf(self, report_data: Dict, filename: str = None) -> str:
        """
        Generate PDF report from analysis data
        
        Args:
            report_data: Report data dictionary
            filename: Optional custom filename
        
        Returns:
            Path to generated PDF file
        """
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"interview_report_{timestamp}.pdf"
        
        filepath = os.path.join(self.output_dir, filename)
        doc = SimpleDocTemplate(filepath, pagesize=A4)
        story = []
        
        # Title
        story.append(Paragraph("AI Interview Analysis Report", self.styles['CustomTitle']))
        story.append(Spacer(1, 0.2*inch))
        
        # Timestamp
        timestamp_str = report_data.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        story.append(Paragraph(f"Generated on: {timestamp_str}", self.styles['Normal']))
        story.append(Spacer(1, 0.3*inch))
        
        # Overall Summary
        story.append(Paragraph("Executive Summary", self.styles['SectionHeader']))
        summary = report_data.get("overall_summary", "No summary available.")
        story.append(Paragraph(summary, self.styles['BodyText']))
        story.append(Spacer(1, 0.2*inch))
        
        # Participants Analysis
        participants = report_data.get("participants", {})
        if participants:
            story.append(Paragraph("Participant Analysis", self.styles['SectionHeader']))
            
            for speaker_id, data in participants.items():
                name = data.get("name", speaker_id)
                story.append(Paragraph(f"<b>{name}</b>", self.styles['Heading3']))
                
                # Metrics table
                metrics_data = [
                    ["Metric", "Score"],
                    ["Confidence", f"{data.get('confidence_score', 0):.2f}"],
                    ["Clarity", f"{data.get('clarity_score', 0):.2f}"],
                    ["Empathy", f"{data.get('empathy_score', 0):.2f}"],
                    ["Engagement", f"{data.get('engagement_score', 0):.2f}"],
                    ["Sentiment", data.get("sentiment", "N/A")],
                    ["Tone", data.get("tone", "N/A")],
                    ["Speaking Pace", data.get("speaking_pace", "N/A")],
                    ["Filler Words", str(data.get("filler_words_count", 0))],
                ]
                
                metrics_table = Table(metrics_data, colWidths=[2*inch, 1.5*inch])
                metrics_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 10),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black)
                ]))
                story.append(metrics_table)
                story.append(Spacer(1, 0.2*inch))
                
                # Key Points
                key_points = data.get("key_points", [])
                if key_points:
                    story.append(Paragraph("<b>Key Points:</b>", self.styles['Normal']))
                    for point in key_points:
                        story.append(Paragraph(f"• {point}", self.styles['BodyText']))
                    story.append(Spacer(1, 0.1*inch))
                
                # Strengths
                strengths = data.get("strengths", [])
                if strengths:
                    story.append(Paragraph("<b>Strengths:</b>", self.styles['Normal']))
                    for strength in strengths:
                        story.append(Paragraph(f"• {strength}", self.styles['BodyText']))
                    story.append(Spacer(1, 0.1*inch))
                
                # Improvements
                improvements = data.get("improvements", [])
                if improvements:
                    story.append(Paragraph("<b>Areas for Improvement:</b>", self.styles['Normal']))
                    for improvement in improvements:
                        story.append(Paragraph(f"• {improvement}", self.styles['BodyText']))
                    story.append(Spacer(1, 0.2*inch))
                
                story.append(PageBreak())
        
        # Overall Assessment
        assessment = report_data.get("assessment", {})
        if assessment:
            story.append(Paragraph("Overall Assessment", self.styles['SectionHeader']))
            
            recommendation = assessment.get("recommendation", "")
            if recommendation:
                story.append(Paragraph(f"<b>Recommendation:</b> {recommendation}", self.styles['BodyText']))
                story.append(Spacer(1, 0.2*inch))
            
            critical_improvements = assessment.get("critical_improvements", [])
            if critical_improvements:
                story.append(Paragraph("<b>Critical Areas for Improvement:</b>", self.styles['Normal']))
                for improvement in critical_improvements:
                    story.append(Paragraph(f"• {improvement}", self.styles['BodyText']))
                story.append(Spacer(1, 0.2*inch))
        
        # Topics and Keywords
        topics = report_data.get("topics", [])
        keywords = report_data.get("keywords", [])
        
        if topics or keywords:
            story.append(Paragraph("Discussion Topics & Keywords", self.styles['SectionHeader']))
            
            if topics:
                story.append(Paragraph("<b>Topics Discussed:</b>", self.styles['Normal']))
                topics_text = ", ".join(topics)
                story.append(Paragraph(topics_text, self.styles['BodyText']))
                story.append(Spacer(1, 0.1*inch))
            
            if keywords:
                story.append(Paragraph("<b>Key Keywords:</b>", self.styles['Normal']))
                keywords_text = ", ".join(keywords)
                story.append(Paragraph(keywords_text, self.styles['BodyText']))
                story.append(Spacer(1, 0.2*inch))
        
        # Detailed Feedback
        detailed_feedback = report_data.get("detailed_feedback", {})
        if detailed_feedback:
            story.append(Paragraph("Detailed Feedback", self.styles['SectionHeader']))
            
            for category, feedback in detailed_feedback.items():
                if feedback:
                    category_title = category.replace("_", " ").title()
                    story.append(Paragraph(f"<b>{category_title}:</b>", self.styles['Normal']))
                    story.append(Paragraph(feedback, self.styles['BodyText']))
                    story.append(Spacer(1, 0.1*inch))
        
        # Build PDF
        doc.build(story)
        return filepath
