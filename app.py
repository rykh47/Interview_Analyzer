"""
Main Streamlit Application
AI Interview Analyzer - Complete Interface
"""
import streamlit as st
import os
import tempfile
from interview_analyzer.audio_processor import AudioProcessor
from interview_analyzer.ai_analyzer import AIAnalyzer
from interview_analyzer.sentiment_analyzer import SentimentAnalyzer
from interview_analyzer.report_generator import ReportGenerator
from interview_analyzer.pdf_generator import PDFGenerator
from interview_analyzer.config import DOMAINS, ROUND_TYPES, ALLOWED_AUDIO_EXTENSIONS, MAX_FILE_SIZE_MB
import time

# Page configuration
st.set_page_config(
    page_title="AI Interview Analyzer",
    page_icon="🎤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'analysis_complete' not in st.session_state:
    st.session_state.analysis_complete = False
if 'report_data' not in st.session_state:
    st.session_state.report_data = None
if 'transcript' not in st.session_state:
    st.session_state.transcript = None

def main():
    """Main application function"""
    
    # Header
    st.title("🎤 AI Interview Analyzer")
    st.markdown("""
    <div style='text-align: center; color: #7f8c8d; margin-bottom: 30px;'>
        <p style='font-size: 18px;'>Transform interviews and discussions into actionable insights</p>
        <p>Powered by Google Gemini AI & OpenAI Whisper</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Domain selection
        domain = st.selectbox(
            "Select Domain",
            options=DOMAINS,
            help="Choose the domain context for better analysis"
        )
        
        # Round type selection
        round_type = st.selectbox(
            "Select Round Type",
            options=ROUND_TYPES,
            help="Specify the type of interview round"
        )
        
        # Feedback tone
        feedback_tone = st.selectbox(
            "Feedback Tone",
            options=["Professional", "Encouraging", "Critical"],
            help="Choose the tone for feedback delivery"
        )
        
        st.markdown("---")
        st.markdown("### 📋 Instructions")
        st.markdown("""
        1. Upload an audio file or paste a text transcript
        2. Select domain and round type
        3. Click 'Analyze Interview'
        4. View comprehensive insights and download report
        """)
        
        # API Key check
        if not os.getenv("GOOGLE_GEMINI_API_KEY"):
            st.warning("⚠️ Please set GOOGLE_GEMINI_API_KEY in your .env file")
    
    # Main content area
    tab1, tab2 = st.tabs(["📁 Upload & Analyze", "📊 Results"])
    
    with tab1:
        st.header("Input Method")
        
        input_method = st.radio(
            "Choose input method:",
            ["Audio File", "Text Transcript"],
            horizontal=True
        )
        
        transcript = None
        
        if input_method == "Audio File":
            st.subheader("Upload Audio File")
            uploaded_file = st.file_uploader(
                "Choose an audio file",
                type=[ext.replace(".", "") for ext in ALLOWED_AUDIO_EXTENSIONS],
                help=f"Supported formats: {', '.join(ALLOWED_AUDIO_EXTENSIONS)}"
            )
            
            if uploaded_file:
                file_size_mb = uploaded_file.size / (1024 * 1024)
                if file_size_mb > MAX_FILE_SIZE_MB:
                    st.error(f"File size exceeds maximum allowed size of {MAX_FILE_SIZE_MB}MB")
                else:
                    st.success(f"✅ File uploaded: {uploaded_file.name} ({file_size_mb:.2f} MB)")
                    
                    if st.button("🎯 Transcribe Audio", type="primary"):
                        with st.spinner("Transcribing audio... This may take a few minutes."):
                            try:
                                audio_processor = AudioProcessor(model_size="base")
                                result = audio_processor.process_uploaded_file(uploaded_file)
                                transcript = result["text"]
                                st.session_state.transcript = transcript
                                
                                st.success("✅ Transcription complete!")
                                st.text_area("Transcription Preview", transcript, height=200, disabled=True)
                            except Exception as e:
                                st.error(f"Error during transcription: {str(e)}")
        
        else:  # Text Transcript
            st.subheader("Enter Text Transcript")
            transcript = st.text_area(
                "Paste or type the interview/discussion transcript here:",
                height=300,
                value=st.session_state.transcript if st.session_state.transcript else "",
                help="Paste the full transcript of the interview or group discussion"
            )
            st.session_state.transcript = transcript
        
        # Analyze button
        if transcript:
            st.markdown("---")
            if st.button("🚀 Analyze Interview", type="primary", use_container_width=True):
                analyze_interview(transcript, domain, round_type, feedback_tone)
    
    with tab2:
        if st.session_state.analysis_complete and st.session_state.report_data:
            display_results(st.session_state.report_data)
        else:
            st.info("👈 Please analyze an interview first using the 'Upload & Analyze' tab")

def analyze_interview(transcript: str, domain: str, round_type: str, feedback_tone: str):
    """Perform comprehensive interview analysis"""
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    try:
        # Step 1: Initialize analyzers
        status_text.text("Initializing analyzers...")
        progress_bar.progress(10)
        
        ai_analyzer = AIAnalyzer()
        sentiment_analyzer = SentimentAnalyzer()
        report_generator = ReportGenerator()
        
        # Step 2: AI Analysis
        status_text.text("Performing AI analysis with Gemini...")
        progress_bar.progress(30)
        
        analysis = ai_analyzer.analyze_conversation(
            transcript=transcript,
            domain=domain,
            round_type=round_type,
            feedback_tone=feedback_tone
        )
        
        # Step 3: Sentiment Analysis
        status_text.text("Analyzing sentiment and tone...")
        progress_bar.progress(60)
        
        # Enhance participant data with sentiment analysis
        if "participants" in analysis:
            for speaker_id, data in analysis["participants"].items():
                # Count filler words
                participant_text = transcript  # In real scenario, extract speaker-specific text
                filler_count = sentiment_analyzer.count_filler_words(participant_text)
                data["filler_words_count"] = filler_count
        
        # Step 4: Generate report
        status_text.text("Generating comprehensive report...")
        progress_bar.progress(80)
        
        report_data = report_generator.generate_report_data(analysis)
        st.session_state.report_data = report_data
        st.session_state.analysis_complete = True
        
        progress_bar.progress(100)
        status_text.text("✅ Analysis complete!")
        time.sleep(1)
        
        st.success("🎉 Analysis completed successfully! Check the 'Results' tab for insights.")
        st.rerun()
        
    except Exception as e:
        st.error(f"❌ Error during analysis: {str(e)}")
        st.exception(e)

def display_results(report_data: dict):
    """Display comprehensive analysis results"""
    
    st.header("📊 Analysis Results")
    
    # Overall Summary
    st.subheader("📝 Executive Summary")
    st.info(report_data.get("overall_summary", "No summary available."))
    
    # Participants Analysis
    participants = report_data.get("participants", {})
    if participants:
        st.markdown("---")
        st.subheader("👥 Participant Analysis")
        
        for speaker_id, data in participants.items():
            with st.expander(f"🔍 {data.get('name', speaker_id)} - Detailed Analysis", expanded=True):
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("Confidence", f"{data.get('confidence_score', 0):.2f}")
                with col2:
                    st.metric("Clarity", f"{data.get('clarity_score', 0):.2f}")
                with col3:
                    st.metric("Empathy", f"{data.get('empathy_score', 0):.2f}")
                with col4:
                    st.metric("Engagement", f"{data.get('engagement_score', 0):.2f}")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("**Sentiment:**", data.get("sentiment", "N/A"))
                    st.write("**Tone:**", data.get("tone", "N/A"))
                    st.write("**Speaking Pace:**", data.get("speaking_pace", "N/A"))
                    st.write("**Filler Words:**", data.get("filler_words_count", 0))
                    st.write("**Communication Quality:**", data.get("communication_quality", "N/A"))
                
                with col2:
                    # Radar chart
                    report_gen = ReportGenerator()
                    radar_fig = report_gen.create_radar_chart(data)
                    st.plotly_chart(radar_fig, use_container_width=True)
                
                # Key Points
                key_points = data.get("key_points", [])
                if key_points:
                    st.write("**Key Points:**")
                    for point in key_points:
                        st.write(f"• {point}")
                
                # Strengths
                strengths = data.get("strengths", [])
                if strengths:
                    st.success("**Strengths:**")
                    for strength in strengths:
                        st.write(f"✅ {strength}")
                
                # Improvements
                improvements = data.get("improvements", [])
                if improvements:
                    st.warning("**Areas for Improvement:**")
                    for improvement in improvements:
                        st.write(f"🔧 {improvement}")
    
    # Visualizations
    st.markdown("---")
    st.subheader("📈 Visualizations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Sentiment Trend
        report_gen = ReportGenerator()
        sentiment_fig = report_gen.create_sentiment_chart(report_data.get("sentiment_trend", []))
        st.plotly_chart(sentiment_fig, use_container_width=True)
    
    with col2:
        # Confidence Comparison
        confidence_fig = report_gen.create_confidence_chart(participants)
        st.plotly_chart(confidence_fig, use_container_width=True)
    
    # Topics and Keywords
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💬 Topics Discussed")
        topics = report_data.get("topics", [])
        if topics:
            for topic in topics:
                st.write(f"• {topic}")
        else:
            st.info("No topics extracted")
    
    with col2:
        st.subheader("🔑 Keywords")
        keywords = report_data.get("keywords", [])
        if keywords:
            keyword_tags = " ".join([f"`{kw}`" for kw in keywords])
            st.markdown(keyword_tags)
        else:
            st.info("No keywords extracted")
    
    # Overall Assessment
    assessment = report_data.get("assessment", {})
    if assessment:
        st.markdown("---")
        st.subheader("🎯 Overall Assessment")
        
        recommendation = assessment.get("recommendation", "")
        if recommendation:
            st.info(f"**Recommendation:** {recommendation}")
        
        critical_improvements = assessment.get("critical_improvements", [])
        if critical_improvements:
            st.warning("**Critical Areas for Improvement:**")
            for improvement in critical_improvements:
                st.write(f"⚠️ {improvement}")
    
    # Detailed Feedback
    detailed_feedback = report_data.get("detailed_feedback", {})
    if detailed_feedback:
        st.markdown("---")
        st.subheader("📋 Detailed Feedback")
        
        for category, feedback in detailed_feedback.items():
            if feedback:
                category_title = category.replace("_", " ").title()
                st.write(f"**{category_title}:**")
                st.write(feedback)
                st.write("")
    
    # Download PDF
    st.markdown("---")
    st.subheader("📥 Download Report")
    
    if st.button("📄 Generate & Download PDF Report", type="primary"):
        with st.spinner("Generating PDF report..."):
            try:
                pdf_gen = PDFGenerator()
                pdf_path = pdf_gen.generate_pdf(report_data)
                
                with open(pdf_path, "rb") as pdf_file:
                    st.download_button(
                        label="⬇️ Download PDF",
                        data=pdf_file.read(),
                        file_name=os.path.basename(pdf_path),
                        mime="application/pdf"
                    )
                st.success("✅ PDF report generated successfully!")
            except Exception as e:
                st.error(f"Error generating PDF: {str(e)}")

if __name__ == "__main__":
    main()

