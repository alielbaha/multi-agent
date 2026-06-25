from anthropic import Anthropic
from app.core.config import settings

client = Anthropic(api_key=settings.anthropic_api_key)

def call_llm(system_prompt:str, user_prompt:str, model:str = "claude-sonnet-4-6"):
    response = client.messages.create(
        model = model,
        max_token = 500,
        system = system_prompt,
        messages = [{"role":"user", "content":system_prompt}],
    )
    return response.content[0].text