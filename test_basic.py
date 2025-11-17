"""
Basic functionality test script
Run this to verify that all modules can be imported and basic functionality works
"""
import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    
    try:
        import streamlit
        print("✅ streamlit")
    except ImportError as e:
        print(f"❌ streamlit: {e}")
        return False
    
    try:
        import whisper
        print("✅ openai-whisper")
    except ImportError as e:
        print(f"⚠️  openai-whisper: {e} (optional for text-only mode)")
    
    try:
        import google.generativeai
        print("✅ google-generativeai")
    except ImportError as e:
        print(f"❌ google-generativeai: {e}")
        return False
    
    try:
        from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
        print("✅ vaderSentiment")
    except ImportError as e:
        print(f"❌ vaderSentiment: {e}")
        return False
    
    try:
        import plotly
        print("✅ plotly")
    except ImportError as e:
        print(f"❌ plotly: {e}")
        return False
    
    try:
        import reportlab
        print("✅ reportlab")
    except ImportError as e:
        print(f"❌ reportlab: {e}")
        return False
    
    return True

def test_local_modules():
    """Test if local modules can be imported"""
    print("\nTesting local modules...")
    
    try:
        from interview_analyzer.config import DOMAINS, ROUND_TYPES
        print("✅ config")
    except ImportError as e:
        print(f"❌ config: {e}")
        return False
    
    try:
        from interview_analyzer.sentiment_analyzer import SentimentAnalyzer
        print("✅ sentiment_analyzer")
    except ImportError as e:
        print(f"❌ sentiment_analyzer: {e}")
        return False
    
    try:
        from interview_analyzer.report_generator import ReportGenerator
        print("✅ report_generator")
    except ImportError as e:
        print(f"❌ report_generator: {e}")
        return False
    
    try:
        from interview_analyzer.pdf_generator import PDFGenerator
        print("✅ pdf_generator")
    except ImportError as e:
        print(f"❌ pdf_generator: {e}")
        return False
    
    # Test AI analyzer (may fail if API key not set)
    try:
        from interview_analyzer.ai_analyzer import AIAnalyzer
        print("✅ ai_analyzer (module loaded)")
    except ImportError as e:
        print(f"❌ ai_analyzer: {e}")
        return False
    
    # Test audio processor (may fail if whisper not installed)
    try:
        from interview_analyzer.audio_processor import AudioProcessor
        print("✅ audio_processor (module loaded)")
    except ImportError as e:
        print(f"⚠️  audio_processor: {e} (optional for text-only mode)")
    
    return True

def test_api_key():
    """Check if API key is configured"""
    print("\nTesting configuration...")
    
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv("GOOGLE_GEMINI_API_KEY")
    if api_key:
        print(f"✅ GOOGLE_GEMINI_API_KEY is set (length: {len(api_key)})")
        return True
    else:
        print("⚠️  GOOGLE_GEMINI_API_KEY not found in .env file")
        print("   Please add your API key to .env file")
        return False

def test_sentiment_analyzer():
    """Test sentiment analyzer functionality"""
    print("\nTesting sentiment analyzer...")
    
    try:
        from interview_analyzer.sentiment_analyzer import SentimentAnalyzer
        analyzer = SentimentAnalyzer()
        
        test_text = "I am very excited about this opportunity!"
        result = analyzer.analyze_sentiment(test_text)
        
        if result and "sentiment" in result:
            print(f"✅ Sentiment analysis works (result: {result['sentiment']})")
            return True
        else:
            print("❌ Sentiment analysis returned unexpected format")
            return False
    except Exception as e:
        print(f"❌ Sentiment analyzer test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 50)
    print("AI Interview Analyzer - Basic Functionality Test")
    print("=" * 50)
    
    all_passed = True
    
    if not test_imports():
        all_passed = False
        print("\n⚠️  Some required packages are missing. Run: pip install -r requirements.txt")
    
    if not test_local_modules():
        all_passed = False
    
    api_key_ok = test_api_key()
    
    if test_sentiment_analyzer():
        print("✅ Sentiment analyzer functionality verified")
    else:
        all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed and api_key_ok:
        print("✅ All tests passed! You're ready to run the application.")
        print("\nNext step: streamlit run app.py")
    elif all_passed:
        print("⚠️  Tests passed, but API key needs to be configured.")
        print("\nNext step: Add GOOGLE_GEMINI_API_KEY to .env file")
    else:
        print("❌ Some tests failed. Please fix the issues above.")
    print("=" * 50)

if __name__ == "__main__":
    main()

