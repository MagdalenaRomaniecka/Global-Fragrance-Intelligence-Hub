import os
from openai import OpenAI

class AudioDataPipeline:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def generate_transcription(self, file_path: str, output_text_path: str) -> bool:
        try:
            with open(file_path, "rb") as audio_file:
                transcript = self.client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                    response_format="text"
                )
            
            with open(output_text_path, "w", encoding="utf-8") as text_file:
                text_file.write(transcript)
            
            return True
        except Exception as e:
            print(f"Error during transcription generation: {e}")
            return False

if __name__ == "__main__":
    api_key = os.environ.get("OPENAI_API_KEY") 
    
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set.")
    else:
        pipeline = AudioDataPipeline(api_key=api_key)
        
        input_m4a = "Data_Strategy_for_Modern_Perfume_Logistics_2.m4a"
        transcription_txt = "Data_Strategy_for_Modern_Perfume_Logistics_2_Transcript.txt"

        if pipeline.generate_transcription(input_m4a, transcription_txt):
            print(f"Successfully generated transcription at {transcription_txt}")