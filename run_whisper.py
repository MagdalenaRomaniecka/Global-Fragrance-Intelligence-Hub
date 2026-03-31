import whisper

print("Loading Whisper model...")
model = whisper.load_model("base") 

print("Transcribing Episode 2...")
result_ep2 = model.transcribe("ep2_audio.mp3")
with open("ep2_raw.txt", "w", encoding="utf-8") as f:
    f.write(result_ep2["text"])

print("Transcribing Episode 5...")
result_ep5 = model.transcribe("ep5_audio.mp3")
with open("ep5_raw.txt", "w", encoding="utf-8") as f:
    f.write(result_ep5["text"])

print("Transcription complete. Check ep2_raw.txt and ep5_raw.txt")