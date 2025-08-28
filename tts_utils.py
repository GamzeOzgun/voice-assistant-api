from gtts import gTTS
import os
import uuid

def text_to_speech(text: str) -> str:
    # Ses dosyası oluşturuluyor
    tts = gTTS(text=text, lang="tr")
    filename = f"response_{uuid.uuid4().hex}.mp3"
    filepath = os.path.join("responses", filename)
    os.makedirs("responses", exist_ok=True)
    tts.save(filepath)
    return f"/responses/{filename}"
