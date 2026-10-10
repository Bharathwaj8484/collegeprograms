
from openai import OpenAI

gpt=OpenAI(
    api_key="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"
)

r= gpt.chat.completions.create(
    model="gpt-3.5"
    messages=[
        {
            "role": "user",
            "content" : "top 10 tech companies"
        }
    ]
)

print(r.choices[0].messages.content)
