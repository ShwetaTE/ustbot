import openai

from openai_bot.settings import OPENAI_API_KEY
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
