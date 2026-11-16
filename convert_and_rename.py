import os
import subprocess

file_mapping = {
    "How_AI_engineers_perfumes_for_your_brain (1).m4a": "ep5_How_AI_engineers_perfumes_for_your_brain.mp3",
    "The_High_Stakes_Economics_Of_Fragrance (1).m4a": "ep6_The_High_Stakes_Economics_Of_Fragrance.mp3",
    "The_Secret_Chemical_Battlefield_of_Luxury_Perfume (1).m4a": "ep7_The_Secret_Chemical_Battlefield_of_Luxury_Perfume.mp3"
}

def process_audio_files(mapping):
    for source_file, target_file in mapping.items():
        if os.path.exists(source_file):
            print(f"Processing: {source_file} -> {target_file}")
            
            command = [
                "ffmpeg", "-y", "-i", source_file,
                "-codec:a", "libmp3lame", "-qscale:a", "2", target_file
            ]
            
            result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            
            if result.returncode == 0:
                print(f"Success: {target_file} generated.")
            else:
                print(f"Error converting {source_file}.")
        else:
            print(f"Warning: Source file '{source_file}' not found.")

if __name__ == "__main__":
    process_audio_files(file_mapping)