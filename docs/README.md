```markdown
# 🎤 AI Interview Analyzer

An intelligent AI-driven system that analyzes interviews and group discussions to provide comprehensive, data-driven feedback on communication skills, sentiment, and performance.

## 🌟 Features

### Core Functionality
- **Multi-Input Support**: Accepts audio files or text transcripts
- **Speech-to-Text**: Powered by OpenAI Whisper for accurate transcription
- **AI-Powered Analysis**: Uses Google Gemini AI for deep understanding
- **Comprehensive Metrics**:
  - Sentiment & Tone Detection
  - Confidence Scoring
  - Clarity & Coherence Analysis
  - Empathy & Emotional Intelligence
  - Filler Word Detection
  - Speaking Pace Analysis
- **Domain-Aware**: Context-aware analysis for Tech, HR, Managerial, and other domains
- **Customizable Feedback**: Professional, Encouraging, or Critical tone options

### Advanced Features
- **Real-time Visualizations**:
  - Sentiment trend over time
  - Confidence vs. Time graphs
  - Communication skills radar charts
- **PDF Report Generation**: Downloadable comprehensive reports
- **Structured Insights**: Key points, strengths, and improvement areas
- **Topic & Keyword Extraction**: Automatic identification of discussion topics

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Interview_Analyzer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Copy the example env file
   cp .env.example .env
   
   # Edit .env and add your Gemini API key
   GOOGLE_GEMINI_API_KEY=your_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Access the application**
   - Open your browser and navigate to `http://localhost:8501`

## 📖 Usage Guide

### Step 1: Input Method
Choose one of two input methods:
- **Audio File**: Upload an audio file (WAV, MP3, MP4, M4A, FLAC, OGG)
- **Text Transcript**: Paste or type the conversation transcript

### Step 2: Configuration
Select from the sidebar:
- **Domain**: Tech, Managerial, HR, Group Discussion, etc.
- **Round Type**: Technical Round, HR Round, Managerial Round, etc.
- **Feedback Tone**: Professional, Encouraging, or Critical

### Step 3: Analyze
Click "Analyze Interview" to process the input and generate insights.

### Step 4: Review Results
View comprehensive analysis including:
- Executive summary
- Participant metrics and scores
- Sentiment trends
- Key points and topics
- Strengths and improvement areas
- Detailed feedback

### Step 5: Download Report
Generate and download a PDF report for offline review.

## 🏗️ Architecture

### System Flow

```
Input (Audio/Text)
    ↓
[Audio Processor] → Transcription (Whisper)
    ↓
[Text Transcript]
    ↓
[AI Analyzer] → Gemini AI Analysis
    ↓
[Sentiment Analyzer] → VADER Sentiment Analysis
    ↓
[Report Generator] → Structured Insights
    ↓
[PDF Generator] → Downloadable Report
    ↓
Output (Dashboard + PDF)
```

### Component Overview

1. **Audio Processor** (`audio_processor.py`)
   - Handles audio file uploads
   - Converts speech to text using OpenAI Whisper
   - Supports multiple audio formats

2. **AI Analyzer** (`ai_analyzer.py`)
   - Integrates with Google Gemini API
   - Performs comprehensive conversation analysis
   - Generates structured insights and recommendations

3. **Sentiment Analyzer** (`sentiment_analyzer.py`)
   - Uses VADER for sentiment analysis
   - Detects filler words
   - Calculates speaking pace

4. **Report Generator** (`report_generator.py`)
   - Creates structured report data
   - Generates interactive visualizations
   - Builds charts and graphs

5. **PDF Generator** (`pdf_generator.py`)
   - Creates professional PDF reports
   - Includes all analysis metrics
   - Ready for download and sharing

6. **Streamlit App** (`app.py`)
   - Main user interface
   - Handles file uploads and user interactions
   - Displays results and visualizations

## 📊 Example Output

### Sample Analysis Report

**Executive Summary:**
The candidate demonstrated strong technical knowledge and clear communication. However, there are opportunities to improve answer structure and reduce filler words.

**Participant Metrics:**
- Confidence Score: 0.75
- Clarity Score: 0.80
- Empathy Score: 0.70
- Engagement Score: 0.85

**Key Strengths:**
- Clear articulation of technical concepts
- Good engagement with the interviewer
- Professional demeanor

**Areas for Improvement:**
- Reduce use of filler words (um, uh)
- Improve answer structure with clear beginning, middle, and end
- Be more concise in responses

## 🔧 Configuration

### Supported Domains
- Tech
- Managerial
- HR
- Group Discussion
- General
- Sales
- Customer Support

### Supported Round Types
- Technical Round
- HR Round
- Managerial Round
- Group Discussion
- Final Round
- Screening Round

### Audio Formats
- WAV
- MP3
- MP4
- M4A
- FLAC
- OGG

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Speech-to-Text**: OpenAI Whisper
- **AI Analysis**: Google Gemini API
- **Sentiment Analysis**: VADER Sentiment
- **Visualization**: Plotly
- **PDF Generation**: ReportLab
- **Orchestration**: LangChain (for future enhancements)

## 📝 API Keys Required

- **Google Gemini API Key**: Required for AI analysis
  - Get your key from: https://makersuite.google.com/app/apikey

## 🎯 Future Enhancements

- Real-time analysis during live interviews
- Multi-language support
- Advanced emotion recognition from voice
- Integration with video analysis
- Custom scoring rubrics
- Batch processing for multiple interviews

## 📄 License

This project is open source and available for educational and commercial use.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For issues, questions, or suggestions, please open an issue on the repository.

---

**Built with ❤️ using AI to make interviews more insightful and fair.**
```
