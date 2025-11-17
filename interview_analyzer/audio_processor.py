"""
Audio Processing Module
Handles speech-to-text conversion using OpenAI Whisper
"""
import whisper
import os
from typing import Optional, Dict
import tempfile

class AudioProcessor:
    def __init__(self, model_size: str = "base"):
        """
        Initialize Whisper model for speech-to-text
        
        Args:
            model_size: Whisper model size (tiny, base, small, medium, large)
        """
        self.model = whisper.load_model(model_size)
    
    def transcribe_audio(self, audio_path: str, language: Optional[str] = None) -> Dict:
        """
        Transcribe audio file to text
        
        Args:
            audio_path: Path to audio file
            language: Optional language code (e.g., 'en', 'hi')
        
        Returns:
            Dictionary with transcription and metadata
        """
        try:
            result = self.model.transcribe(
                audio_path,
                language=language,
                task="transcribe",
                verbose=False
            )
            
            return {
                "text": result["text"],
                "segments": result.get("segments", []),
                "language": result.get("language", "unknown")
            }
        except Exception as e:
            raise Exception(f"Error transcribing audio: {str(e)}")
    
    def process_uploaded_file(self, uploaded_file) -> Dict:
        """
        Process uploaded audio file from Streamlit
        
        Args:
            uploaded_file: Streamlit uploaded file object
        
        Returns:
            Transcription result dictionary
        """
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name
        
        try:
            result = self.transcribe_audio(tmp_path)
            return result
        finally:
            # Clean up temporary file
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
