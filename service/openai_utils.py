import openai

openai.api_key = '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'

def openai_complete(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    json_string = completion.choices[0].message['content']
    return json_string
