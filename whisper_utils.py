import whisper

def transcribe_audio_file(path: str) -> str:
    
    model = whisper.load_model("medium")

    
    result = model.transcribe(path)

    
    return result["text"]
