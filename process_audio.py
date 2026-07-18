import whisper
import os

def execute_transcription():
    audio_files = [
        "masterclass_ep1_audio.mp3",
        "masterclass_ep2_audio.mp3",
        "masterclass_ep3_audio.mp3"
    ]
    
    for audio_path in audio_files:
        if os.path.exists(audio_path):
            print(f"Transcribing: {audio_path}")
            model = whisper.load_model("base")
            transcript_result = model.transcribe(audio_path)
            
            output_filename = audio_path.replace(".mp3", "_transcript.md")
            with open(output_filename, "w", encoding="utf-8") as file_handler:
                file_handler.write(transcript_result["text"])
            
            print(f"Completed: {output_filename}")
        else:
            print(f"Missing target file: {audio_path}")

if __name__ == "__main__":
    execute_transcription()