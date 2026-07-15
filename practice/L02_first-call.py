#Needs to be more clear on what to run in the class session

import anthropic
from dotenv import load_dotenv

load_dotenv()   # reads .env so the key works from any terminal or the IDE Run button

client = anthropic.Anthropic()

resp = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=1024, 
    system="You are terse assistant. Answer in one sentence.",
    messages=[
        {"role": "user", "content": "What is prompt injection?"}, 
    ],
)

print(resp.content[0].text)