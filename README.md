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
# 🎤 AI Interview Analyzer

An intelligent AI-driven system that analyzes interviews and group discussions to provide comprehensive, data-driven feedback on communication skills, sentiment, and performance.

**For full documentation, see `docs/README.md`.**

## Quick Links

- 📖 **Full Documentation:** [`docs/README.md`](docs/README.md)
- 🚀 **Quick Start:** [`docs/QUICK_START.md`](docs/QUICK_START.md)
- 📊 **Project Overview:** [`docs/PROJECT_SUMMARY.md`](docs/PROJECT_SUMMARY.md)
- 🔄 **System Architecture:** [`docs/FLOW_DIAGRAM.md`](docs/FLOW_DIAGRAM.md)
- 📋 **Example Output:** [`docs/EXAMPLE_OUTPUT.md`](docs/EXAMPLE_OUTPUT.md)

## Installation

```bash
python setup.py
```

or manually:

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## Repository Structure

```
Interview_Analyzer/
├── app.py                 # Main Streamlit application
├── setup.py              # Setup script
├── test_basic.py         # Basic tests
├── requirements.txt      # Python dependencies
├── .env                  # Local environment variables (not in git)
├── .env.example         # Template for .env
├── interview_analyzer/   # Core package
│   ├── __init__.py
│   ├── ai_analyzer.py
│   ├── audio_processor.py
│   ├── config.py
│   ├── pdf_generator.py
│   ├── report_generator.py
│   └── sentiment_analyzer.py
├── docs/                 # Full documentation
│   ├── README.md
│   ├── QUICK_START.md
│   ├── PROJECT_SUMMARY.md
│   ├── FLOW_DIAGRAM.md
│   └── EXAMPLE_OUTPUT.md
├── outputs/              # Generated reports (ignored by git)
└── uploads/              # Uploaded audio files (ignored by git)
```

## Features

- ✅ Multi-input support (audio files or text transcripts)
- ✅ Speech-to-text transcription (OpenAI Whisper)
- ✅ AI-powered analysis (Google Gemini API)
- ✅ Sentiment & tone detection (VADER)
- ✅ Comprehensive metrics (confidence, clarity, empathy, engagement)
- ✅ Interactive visualizations (Plotly)
- ✅ PDF report generation (ReportLab)
- ✅ Domain-aware feedback (Tech, HR, Managerial, etc.)

## Next Steps

1. Add your `GOOGLE_GEMINI_API_KEY` to `.env`
2. See [`docs/QUICK_START.md`](docs/QUICK_START.md) for detailed setup
3. Run `streamlit run app.py`

---

**Built with ❤️ to make interviews more insightful, fair, and helpful for everyone.**
### Advanced Features

- **Real-time Visualizations**:
