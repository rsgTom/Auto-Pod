import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_script(persona, episode_theme, intro_clip, episode_num, guest_name, guest_intro, commercial_break):
    model="gpt-3.5-turbo",
    prompt=f"{persona}{episode_theme}{intro_clip}{episode_num}{guest_name}{guest_intro}{commercial_break}"
    max_tokens=150

    response=openai.Completion.create(
        model=model,
        prompt=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=max_tokens
    )

    response_text = response['choices'][0]['text'].strip()
    return response_text
