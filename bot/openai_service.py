import openai

from openai_bot.settings import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY


def ask_openai(prompt,user_email):
    print("inside ask openai", prompt)
    # personalized_prompt = f"Please mention the user with the email {user_email} in your response. The question is: {prompt}. Modify your answer to directly address the user if needed. do not mention Dear, do not add user_email in (), you can say Hello"

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
