import openai
# from dotenv import load_dotenv
# import os

# # Load the .env file when the script is imported
# load_dotenv()

# # Set up OpenAI API key
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# from openai_bot.settings import OPENAI_API_KEY
OPENAI_API_KEY="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" 

openai.api_key = OPENAI_API_KEY


def ask_openai(prompt):
    print("inside ask openai", prompt)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=200,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"
