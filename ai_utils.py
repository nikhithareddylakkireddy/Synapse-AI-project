from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1",
)

def ask_ai(prompt):

    completion = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message.content