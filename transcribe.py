import whisper
import os

def find_audio_file():
    """
    Auto-detects any .mp3 or .wav file in the project directories.
    """
    print("🔍 Searching for audio files in the project...")
    
    # Walk through all folders starting from current directory
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.lower().endswith(('.mp3', '.wav')):
                full_path = os.path.join(root, file)
                print(f"✅ FOUND AUDIO FILE: {full_path}")
                return full_path
    return None

def transcribe_smart():
    # 1. Find the file automatically
    audio_path = find_audio_file()
    
    if not audio_path:
        print("❌ CRITICAL ERROR: No .mp3 or .wav files found in this folder or subfolders.")
        print("   Please check if the file is truly inside the project folder.")
        print(f"   Current working directory: {os.getcwd()}")
        return

    # 2. Load Whisper
    print("⏳ Loading Whisper model... (This runs locally)")
    
    try:
        model = whisper.load_model("base")
        print(f"🎧 Transcribing: {audio_path}")
        result = model.transcribe(audio_path)
        
        output_file = "podcast_transcript.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result["text"])
            
        print(f"✅ SUCCESS! Transcript saved to: {output_file}")
        print("👉 You can now open the text file to check timestamps.")
        
    except Exception as e:
        print(f"❌ ERROR: {e}")

if __name__ == "__main__":
    transcribe_smart()