```markdown
# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

**Note:** If you encounter issues with `pyaudio` on Windows, you can skip it as it's optional. The core functionality works without it.

### Step 2: Set Up API Key

1. Get your Google Gemini API key from: https://makersuite.google.com/app/apikey

2. Create a `.env` file in the project root:
   ```
   GOOGLE_GEMINI_API_KEY=your_api_key_here
   ```

### Step 3: Run the Application

```bash
streamlit run app.py
```

### Step 4: Open in Browser

The app will automatically open at `http://localhost:8501`

---

## 📝 First Analysis

### Option 1: Upload Audio File
1. Go to "Upload & Analyze" tab
2. Select "Audio File"
3. Upload a WAV, MP3, or other supported format
4. Click "Transcribe Audio"
5. Wait for transcription
6. Click "Analyze Interview"

### Option 2: Use Text Transcript
1. Go to "Upload & Analyze" tab
2. Select "Text Transcript"
3. Paste your interview transcript
4. Click "Analyze Interview"

### View Results
1. Go to "Results" tab
2. Review comprehensive analysis
3. Download PDF report if needed

---

## 🎯 Example Transcript

Try this sample transcript to test the system:

```
Interviewer: Good morning! Thank you for coming in today. Let's start with a brief introduction.

Candidate: Good morning! Um, thank you for having me. So, I'm John, and I've been working as a software engineer for about five years now. I've worked primarily with Python and JavaScript, and I'm really excited about this opportunity.

Interviewer: Great! Can you tell me about a challenging project you've worked on recently?

Candidate: Yeah, so, um, we had this project where we needed to scale our application to handle, like, ten times more traffic. It was really challenging because, you know, we had to refactor a lot of the code. We used microservices architecture and implemented caching strategies. The result was pretty good - we reduced response time by about 60 percent.

Interviewer: That's impressive! How did you handle the database optimization?

Candidate: Well, we, um, we looked at the query patterns first. Then we added indexes where needed and implemented read replicas. We also used connection pooling to manage database connections more efficiently.
```

---

## ⚙️ Configuration Tips

### Domain Selection
- **Tech**: For technical interviews focusing on coding, algorithms, system design
- **HR**: For behavioral and cultural fit interviews
- **Managerial**: For leadership and management roles
- **Group Discussion**: For group assessment scenarios

### Feedback Tone
- **Professional**: Balanced, objective feedback
- **Encouraging**: Warm, supportive tone highlighting strengths
- **Critical**: Detailed analysis focusing on improvement areas

---

## 🐛 Troubleshooting

### Issue: "Gemini API key not found"
**Solution:** Make sure your `.env` file exists and contains:
```
GOOGLE_GEMINI_API_KEY=your_actual_key_here
```

### Issue: Audio transcription fails
**Solution:** 
- Check audio file format (WAV, MP3, etc.)
- Ensure file size is under 100MB
- Try a different audio file

### Issue: "Module not found" errors
**Solution:**
```bash
pip install -r requirements.txt --upgrade
```

### Issue: Whisper model download is slow
**Solution:** The first run downloads the model (~150MB). Subsequent runs will be faster.

---

## 📊 Understanding the Results

### Scores (0.0 - 1.0)
- **0.0-0.4**: Needs significant improvement
- **0.4-0.6**: Average, room for improvement
- **0.6-0.8**: Good performance
- **0.8-1.0**: Excellent performance

### Sentiment
- **Positive**: Confident, enthusiastic, engaging
- **Neutral**: Balanced, professional
- **Negative**: Anxious, uncertain, disengaged

### Filler Words
- **0-5**: Excellent
- **5-10**: Good
- **10-20**: Needs improvement
- **20+**: Significant improvement needed

---

## 💡 Tips for Best Results

1. **Clear Audio**: For best transcription, use clear audio with minimal background noise
2. **Complete Transcripts**: Include the full conversation for comprehensive analysis
3. **Domain Context**: Select the appropriate domain for context-aware feedback
4. **Multiple Speakers**: The system can analyze multiple participants in group discussions

---

## 🎓 Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [FLOW_DIAGRAM.md](FLOW_DIAGRAM.md) to understand the system architecture
- Review [EXAMPLE_OUTPUT.md](EXAMPLE_OUTPUT.md) for sample analysis reports

Happy analyzing! 🎤✨
```
