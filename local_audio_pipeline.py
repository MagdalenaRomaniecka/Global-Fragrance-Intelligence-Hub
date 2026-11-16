import os
import whisper

class AudioTranscriptionPipeline:
    def __init__(self, model_size: str = "base"):
        self.model = whisper.load_model(model_size)

    def transcribe_files(self, file_names: list) -> None:
        for name in file_names:
            clean_name = name.replace(" ", "_")
            audio_path = f"{clean_name}.m4a"
            output_path = f"{clean_name}_Transcript.txt"

            if not os.path.exists(audio_path):
                audio_path_spaces = f"{name.replace('_', ' ')}.m4a"
                if os.path.exists(audio_path_spaces):
                    audio_path = audio_path_spaces
                else:
                    print(f"File not found: {audio_path}")
                    continue

            if os.path.exists(output_path):
                print(f"Skipping (already transcribed): {output_path}")
                continue

            print(f"Transcribing: {audio_path}...")
            
            try:
                result = self.model.transcribe(audio_path)
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(result["text"])
                print(f"Successfully saved: {output_path}")
            except Exception as e:
                print(f"Failed to transcribe {audio_path}: {e}")

if __name__ == "__main__":
    target_files = [
        "How_Data_Architecture_Fixes_Online_Perfume_Sales",
        "How_Data_Architecture_Saved_Perfume",
        "The_Brutal_Economics_of_Luxury_Perfume"
    ]

    pipeline = AudioTranscriptionPipeline()
    pipeline.transcribe_files(target_files)