
from transformers import pipeline
import openai
import json

# Load OpenAI configuration
with open("config.json", "r") as config_file:
    config = json.load(config_file)
openai.api_key = config["openai_api_key"]

text_pipeline = pipeline("text-classification", model="roberta-base")

def analyze_text(chat_text: str):
    result = text_pipeline(chat_text)
    return result

def analyze_with_openai(chat_text: str):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant helping to detect OCD tendencies in user input."},
                {"role": "user", "content": chat_text}
            ],
            max_tokens=150
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return {"error": str(e)}
