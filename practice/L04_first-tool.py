import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()
MODEL = "claude-haiku-4-5"   # cheap for practice reps; code is identical on opus

# The real function. Read-only, no side effects — least privilege by design.
ACCOUNTS = {"alice": 120, "bob": 5}
def get_balance(user):
    return str(ACCOUNTS.get(user.lower(), "unknown user"))

tools = [{
    "name": "get_balance",
    "description": "Look up a user's account balance in dollars.",
    "input_schema": {
        "type": "object",
        "properties": {"user": {"type": "string"}},
        "required": ["user"],
    },
}]

messages = [{"role": "user", "content": "How much does Alice have?"}]
resp = client.messages.create(model=MODEL, max_tokens=1024, tools=tools, messages=messages)

print("stop_reason:", resp.stop_reason)          # -> "tool_use"
for block in resp.content:
    if block.type == "tool_use":
        print("model asked to call:", block.name, block.input)
        result = get_balance(block.input["user"])   # YOUR code runs it
        messages.append({"role": "assistant", "content": resp.content})
        messages.append({"role": "user", "content": [{
            "type": "tool_result", "tool_use_id": block.id, "content": result,
        }]})

# Loop back so the model can turn the result into an answer
final = client.messages.create(model=MODEL, max_tokens=1024, tools=tools, messages=messages)
print("final answer:", final.content[0].text)