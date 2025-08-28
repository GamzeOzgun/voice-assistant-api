import whisper

def transcribe_audio_file(path: str) -> str:
    # Whisper modeli yükleniyor (daha doğru sonuç için 'medium' seçildi)
    model = whisper.load_model("medium")

    # Ses dosyası metne çevriliyor
    result = model.transcribe(path)

    # Metin döndürülüyor
    return result["text"]
