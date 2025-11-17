"""
Setup script for AI Interview Analyzer
"""
import os
import subprocess
import sys

def check_python_version():
    """Check if Python version is 3.8 or higher"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    print(f"✅ Python version: {sys.version}")

def install_dependencies():
    """Install required packages"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Error installing dependencies")
        sys.exit(1)

def check_env_file():
    """Check if .env file exists"""
    if not os.path.exists(".env"):
        print("⚠️  .env file not found")
        if os.path.exists(".env.example"):
            print("📝 Creating .env from .env.example...")
            with open(".env.example", "r") as example:
                with open(".env", "w") as env_file:
                    env_file.write(example.read())
            print("✅ .env file created. Please add your GOOGLE_GEMINI_API_KEY")
        else:
            print("❌ .env.example not found")
    else:
        print("✅ .env file exists")

def create_directories():
    """Create necessary directories"""
    directories = ["outputs", "uploads"]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ Created directory: {directory}")

def main():
    """Main setup function"""
    print("🚀 Setting up AI Interview Analyzer...\n")
    
    check_python_version()
    print()
    
    create_directories()
    print()
    
    check_env_file()
    print()
    
    install_dependencies()
    print()
    
    print("✅ Setup complete!")
    print("\n📋 Next steps:")
    print("1. Add your GOOGLE_GEMINI_API_KEY to the .env file")
    print("2. Run: streamlit run app.py")
    print("3. Open http://localhost:8501 in your browser")

if __name__ == "__main__":
    main()

