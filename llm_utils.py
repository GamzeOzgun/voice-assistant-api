from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Açık erişimli ve stabil model
model_name = "EleutherAI/gpt-neo-1.3B"

# Tokenizer ve model yükleniyor
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Text generation pipeline kuruluyor
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device=0  # CPU kullanımı
)

def generate_answer(prompt: str) -> str:
    prompt_lower = prompt.lower().strip()

    # 🔒 Kritik sorulara sabit yanıt
    if "sipariş" in prompt_lower or "siparişim" in prompt_lower:
        return "Siparişiniz 2-3 gün içerisinde elinize ulaşacaktır."

    # 🔓 Diğer sorular için LLM ile üretim
    safe_prompt = f"Soru: {prompt.strip()}\nCevap:"
    result = generator(
        safe_prompt,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.7,
        top_p=0.95
    )[0]["generated_text"]

    # Yanıtı sadece 'Cevap:' kısmından sonrasını al
    answer = result.split("Cevap:")[-1].strip()

    # Eğer model 'Soru:' kısmını tekrar ediyorsa, onu temizle
    if "Soru:" in answer:
        answer = answer.split("Soru:")[0].strip()

    return answer
