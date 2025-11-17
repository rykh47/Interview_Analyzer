"""
Configuration file for AI Interview Analyzer
"""
import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
GEMINI_API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY", "")

# Domain and Round Types
DOMAINS = [
    "Tech",
    "Managerial",
    "HR",
    "Group Discussion",
    "General",
    "Sales",
    "Customer Support"
]

ROUND_TYPES = [
    "Technical Round",
    "HR Round",
    "Managerial Round",
    "Group Discussion",
    "Final Round",
    "Screening Round"
]

# Analysis Configuration
SENTIMENT_CATEGORIES = ["Positive", "Neutral", "Negative", "Confident", "Nervous", "Calm", "Enthusiastic"]
EMOTION_CATEGORIES = ["Empathy", "Confidence", "Clarity", "Engagement", "Professionalism"]

# File Upload Settings
ALLOWED_AUDIO_EXTENSIONS = [".wav", ".mp3", ".mp4", ".m4a", ".flac", ".ogg"]
MAX_FILE_SIZE_MB = 100

# Output Settings
OUTPUT_DIR = "outputs"
UPLOAD_DIR = "uploads"
