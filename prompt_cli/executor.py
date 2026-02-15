import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def run_prompt(prompt: str, model: str = "gpt-4") -> str:
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content
