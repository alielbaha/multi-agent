from app.core.config import settings
from groq import Groq

client = Groq(api_key=settings.groq_api_key)


def call_llm(system_prompt: str, user_prompt: str, model: str = "openai/gpt-oss-120b"):
    response = client.chat.completions.create(
        model=model,
        max_tokens=500,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        reasoning_effort="low",
    )
    return response.choices[0].message.content
