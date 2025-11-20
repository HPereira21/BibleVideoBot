import requests
import openai
import os

# SET YOUR OPENAI API KEY HERE OR IN ENVIRONMENT VARIABLES
# os.environ["OPENAI_API_KEY"] = "sk-..." 
# Or paste it directly below (keep it private!):
OPENAI_KEY = "YOUR_OPENAI_API_KEY_HERE"

client = openai.OpenAI(api_key=OPENAI_KEY)

def get_bible_verse(reference, language="pt"):
    """
    Fetches verse text from bible-api.com (Free, no key required)
    """
    # bible-api.com uses 'almeida' for Portuguese and 'web' (World English Bible) for English
    translation = "almeida" if language == "pt" else "web"
    
    url = f"https://bible-api.com/{reference}?translation={translation}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['text'].strip(), data['reference']
    else:
        raise Exception(f"Could not find verse: {reference}")

def generate_devotional_script(verse_text, verse_ref, language="pt"):
    """
    Uses GPT-4o-mini (cheap & fast) to write a night-time devotional.
    """
    if language == "pt":
        system_prompt = "You are a calm, soothing Christian narrator creating content for a night-time prayer channel."
        user_prompt = (
            f"Escreva um roteiro curto, calmo e reconfortante para um vídeo de YouTube Shorts. "
            f"O tema é o versículo bíblico: '{verse_text}' ({verse_ref}). "
            f"Comece lendo o versículo claramente. Depois, dê uma breve reflexão de 2 frases sobre paz e descanso em Deus. "
            f"Termine com 'Amém' e 'Boa noite'. "
            f"Não use emojis. O tom deve ser muito relaxante, para dormir."
        )
    else:
        system_prompt = "You are a calm, soothing Christian narrator creating content for a night-time prayer channel."
        user_prompt = (
            f"Write a short, calm, and soothing script for a YouTube Short. "
            f"The topic is the bible verse: '{verse_text}' ({verse_ref}). "
            f"Start by reading the verse clearly. Then provide a brief 2-sentence reflection on peace and rest in God. "
            f"End with 'Amen' and 'Good night'. "
            f"Do not use emojis. The tone must be very relaxing, suitable for sleeping."
        )

    response = client.chat.completions.create(
        model="gpt-4o-mini", # Very cheap model
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    
    return response.choices[0].message.content.strip()