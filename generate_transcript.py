import whisper
import warnings
import os

# Suppress warnings for cleaner terminal output
warnings.filterwarnings("ignore")

def transcribe_audio_pipeline(audio_path, output_path):
    """
    AI Orchestration: Loads OpenAI's Whisper model and transcribes 
    the generated market briefing audio into a timestamped markdown file.
    """
    if not os.path.exists(audio_path):
        print(f"Error: Audio file '{audio_path}' not found!")
        return

    print("🚀 Loading Whisper AI model (base)...")
    # Using 'base' model - it's fast and highly accurate for English
    model = whisper.load_model("base") 
    
    print(f"🎙️ Transcribing '{audio_path}'... This may take a minute.")
    result = model.transcribe(audio_path)
    
    print("✅ Transcription complete! Formatting and saving...")
    
    # Save the result with professional timestamps
    with open(output_path, "w", encoding="utf-8") as file:
        file.write("# 🎧 Episode 3: Raw AI Transcription (Whisper)\n")
        file.write("> *Automated transcription pipeline using OpenAI Whisper.*\n\n")
        
        for segment in result["segments"]:
            # Format time (e.g., 00:15)
            start_m, start_s = divmod(int(segment["start"]), 60)
            end_m, end_s = divmod(int(segment["end"]), 60)
            
            timestamp = f"[{start_m:02d}:{start_s:02d} - {end_m:02d}:{end_s:02d}]"
            text = segment["text"].strip()
            
            file.write(f"**{timestamp}** {text}\n\n")
            
    print(f"🎉 Success! Transcript saved to: {output_path}")

if __name__ == "__main__":
    # Define input (your NotebookLM audio) and output files
    AUDIO_FILE = "ep3_europe_barbell.mp3"
    OUTPUT_FILE = "ep3_whisper_transcript_EN.md"
    
    transcribe_audio_pipeline(AUDIO_FILE, OUTPUT_FILE)