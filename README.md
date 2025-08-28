Voice Assistant API – Sesli Yanıt Sistemi

Bu proje, e-ticaret firmalarının müşteri hizmetlerinde kullanılmak üzere hazırlanmış basit bir sesli asistan servisidir. Kullanıcı sesli bir soru sorar, bu soru yazıya çevrilir ve sistem uygun bir yanıt üretir. Yanıt hem metin hem de ses olarak döndürülür.

Özellikler
- Ses dosyasını yazıya çevirir (Whisper)
- Yazıya anlamlı yanıt verir (GPT-Neo)
- Yanıtı ses dosyasına dönüştürür (gTTS)
- Swagger arayüzünden test edilebilir
- JSON formatında çıktı üretir

Kullanılan Teknolojiler
- FastAPI (API altyapısı)
- Whisper (ses tanıma)
- Transformers (LLM modeli)
- gTTS (metni sese çevirme)
- Uvicorn (sunucu)

Proje Yapısı
voice_assistant_project/
├── main.py
├── whisper_utils.py
├── llm_utils.py
├── tts_utils.py
├── requirements.txt
├── temp/               # Geçici ses dosyaları
└── responses/          # Yanıt ses dosyaları

Kurulum
1. Depoyu klonlayın
   git clone https://github.com/kullaniciadi/voice-assistant-api.git
   cd voice-assistant-api

2. Sanal ortam oluşturun
   python -m venv venv

3. Ortamı aktif edin
   Windows: .\venv\Scripts\Activate.ps1
   Mac/Linux: source venv/bin/activate

4. Gerekli paketleri yükleyin
   pip install -r requirements.txt

requirements.txt
fastapi
uvicorn
whisper
transformers
torch
gtts

API’yi Başlatma
python -m uvicorn main:app --reload

Tarayıcıdan test için:
http://127.0.0.1:8000/docs

API Kullanımı
- Endpoint: POST /ask_assistant
- Girdi: Ses dosyası (.wav, .mp3)
- Çıktı örneği:

{
  "transcribed_text": "Siparişim nerede?",
  "assistant_response": "Siparişiniz 2-3 gün içinde elinize ulaşacaktır.",
  "response_audio_url": "/responses/response_abc123.mp3"
}

Notlar
- Bu proje sadece bir prototiptir, gerçek veritabanı veya sipariş sistemiyle bağlantısı yoktur.
- Yanıtlar örnek senaryolara göre hazırlanmıştır.
- Whisper modeli “medium” seçilmiştir.
- Yanıt sesleri responses/ klasöründe saklanır.
