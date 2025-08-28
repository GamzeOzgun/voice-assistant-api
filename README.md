# Voice Assistant API – Sesli Yanıt Sistemi

---

## Özellikler

- Ses dosyasını yazıya çevirir (Whisper)  
- Yazıya anlamlı yanıt verir (GPT-Neo)  
- Yanıtı ses dosyasına dönüştürür (gTTS)  
- Swagger arayüzünden test edilebilir  
- JSON formatında çıktı üretir

---

## Kullanılan Teknolojiler

- **FastAPI** – API altyapısı  
- **Whisper** – Ses tanıma  
- **Transformers** – LLM modeli  
- **gTTS** – Metni sese çevirme  
- **Uvicorn** – Sunucu çalıştırma

---

## Proje Yapısı

```
voice_assistant_project/
├── main.py
├── whisper_utils.py
├── llm_utils.py
├── tts_utils.py
├── requirements.txt
├── README.md
├── temp/               # Geçici ses dosyaları
└── responses/          # Yanıt ses dosyaları
```

---

## Kurulum

### 1. Depoyu klonlayın

```bash
git clone https://github.com/kullaniciadi/voice-assistant-api.git
cd voice-assistant-api
```

### 2. Sanal ortam oluşturun

```bash
python -m venv venv
```

### 3. Ortamı aktif edin

**Windows:**

```powershell
.\venv\Scripts\Activate.ps1
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 4. Gerekli paketleri yükleyin

```bash
pip install -r requirements.txt
```

---

## requirements.txt

```txt
fastapi
uvicorn
whisper
transformers
torch
gtts
```

---

## API’yi Başlatma

```bash
python -m uvicorn main:app --reload
```

Tarayıcıdan test için:

```
http://127.0.0.1:8000/docs
```

---

## API Kullanımı

- **Endpoint:** `POST /ask_assistant`  
- **Girdi:** Ses dosyası (.wav, .mp3)  
- **Çıktı örneği:**

```json
{
  "transcribed_text": "Siparişim nerede?",
  "assistant_response": "Siparişiniz 2-3 gün içinde elinize ulaşacaktır.",
  "response_audio_url": "/responses/response_abc123.mp3"
}
```

Yanıt ses dosyasını `response_audio_url` üzerinden dinleyebilirsiniz.

---

##  Kurulum Uyarısı

Proje ilk kez çalıştırıldığında, `venv/` klasörü eksikse veya silinmişse, bazı modüller (`fastapi`, `whisper`, `transformers` vb.) `main.py` içinde tanınmayabilir. Bu durumda:

1. Yeni bir sanal ortam oluşturun:

```bash
python -m venv venv
```

2. Ortamı aktif edin:

```powershell
.\venv\Scripts\Activate.ps1
```

3. Gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt
```

> Bu adımlar tamamlandığında `main.py` dosyası sorunsuz çalışacaktır.

---

## Notlar

- Bu proje bir prototiptir, gerçek veritabanı veya sipariş sistemiyle bağlantısı yoktur.  
- Yanıtlar örnek senaryolara göre hazırlanmıştır.  
- Whisper modeli `"medium"` olarak seçilmiştir.  
- Yanıt sesleri `responses/` klasöründe saklanır.
