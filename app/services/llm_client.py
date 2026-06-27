from app.core.config import settings
from groq import Groq

client = Groq(api_key=settings.groq_api_key)


def call_llm(
    system_prompt: str, user_prompt: str, model: str = "llama-3.3-70b-versatile"
):
    response = client.chat.completions.create(
        model=model,
        max_tokens=500,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.content[0].text
