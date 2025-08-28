from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import os

from whisper_utils import transcribe_audio_file
from llm_utils import generate_answer
from tts_utils import text_to_speech

app = FastAPI()

@app.post("/ask_assistant")
async def ask_assistant(file: UploadFile = File(...)):
    # Geçici klasör ve dosya yolu
    temp_dir = "temp"
    os.makedirs(temp_dir, exist_ok=True)
    temp_path = os.path.join(temp_dir, file.filename)

    # Dosyayı kaydet
    with open(temp_path, "wb") as f:
        f.write(await file.read())

    # Ses dosyasını metne çevir
    transcribed_text = transcribe_audio_file(temp_path)

    # Eğer metin boşsa, hata döndür
    if not transcribed_text.strip():
        return JSONResponse(
            status_code=400,
            content={
                "error": "Ses dosyasından anlamlı metin çıkarılamadı.",
                "transcribed_text": transcribed_text
            }
        )

    # Metne göre yanıt üret
    assistant_response = generate_answer(transcribed_text)

    # Yanıtı sese çevir
    response_audio_url = text_to_speech(assistant_response)

    # JSON yanıtı döndür
    return JSONResponse({
        "transcribed_text": transcribed_text,
        "assistant_response": assistant_response,
        "response_audio_url": response_audio_url
    })
