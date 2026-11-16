import os
from pydub import AudioSegment
from openai import OpenAI

class AudioDataPipeline:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def convert_m4a_to_mp3(self, input_file_path: str, output_file_path: str) -> bool:
        try:
            audio = AudioSegment.from_file(input_file_path, format="m4a")
            audio.export(output_file_path, format="mp3")
            return True
        except Exception as e:
            print(f"Error during audio conversion: {e}")
            return False

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
        converted_mp3 = "Data_Strategy_for_Modern_Perfume_Logistics_2.mp3"
        transcription_txt = "Data_Strategy_for_Modern_Perfume_Logistics_2_Transcript.txt"

        if pipeline.convert_m4a_to_mp3(input_m4a, converted_mp3):
            pipeline.generate_transcription(converted_mp3, transcription_txt)