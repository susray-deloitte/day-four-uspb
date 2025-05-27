import os
from dotenv import load_dotenv
import openai

load_dotenv()

def get_chatbot_response(prompt):
    try:
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error in get_chatbot_response: {e}")
        return "An error occurred while processing your request."