import subprocess
import sys
import os

def install_requirements():
    print("Checking and installing requirements...")
    try:
        # Check if pip is available
        subprocess.check_call([sys.executable, "-m", "pip", "--version"])
    except subprocess.CalledProcessError:
        print("Error: pip is not installed. Please install pip first.")
        sys.exit(1)

    try:
        # Install requirements
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Requirements installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")
        sys.exit(1)

def main():
    # Install requirements first
    install_requirements()
    
    print("\nStarting Topics Updater...")
    # Import and run the main program
    try:
        from topics_updater import TopicsUpdater
        app = TopicsUpdater()
        app.run()
    except Exception as e:
        print(f"Error starting the application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
