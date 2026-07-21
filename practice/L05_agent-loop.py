import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()
MODEL = "claude-haiku-4-5"   # cheap for practice; code is identical on opus

# A tiny read-only "price book" the model must query item by item.
PRICES = {"widget": 5, "gadget": 12, "gizmo": 3}
def get_price(item):
    return str(PRICES.get(item.lower(), "unknown item"))

tools = [{
    "name": "get_price",
    "description": "Look up the price of a single item in dollars.",
    "input_schema": {
        "type": "object",
        "properties": {"item": {"type": "string"}},
        "required": ["item"],
    },
}]

messages = [{"role": "user",
             "content": "What's the total price of a widget, a gadget, and a gizmo?"}]

# THE AGENT LOOP — keep going until the model stops asking for tools
for step in range(10):                     # loop cap: never unbounded
    resp = client.messages.create(model=MODEL, max_tokens=1024,
                                  tools=tools, messages=messages)
    print(f"step {step}: stop_reason =", resp.stop_reason)

    if resp.stop_reason != "tool_use":
        print("final answer:", resp.content[0].text)
        break

    messages.append({"role": "assistant", "content": resp.content})
    results = []
    for block in resp.content:
        if block.type == "tool_use":
            print("  model asked:", block.name, block.input)
            result = get_price(block.input["item"])   # YOUR code runs it
            results.append({"type": "tool_result",
                            "tool_use_id": block.id, "content": result})
    messages.append({"role": "user", "content": results})