import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()
MODEL = "claude-haiku-4-5"   # cheap for practice; identical on opus

DOCS = {
    "refund":   "Refunds are available within 30 days of purchase with a receipt.",
    "shipping": "Standard shipping takes 5-7 business days; express takes 2 days.",
    "warranty": "All widgets carry a 1-year limited warranty against defects.",
}

def retrieve(query):
    for key, text in DOCS.items():
        if key in query.lower():
            return key, text
    return None, ""

def rag_answer(user_q):
    doc_id, context = retrieve(user_q)
    prompt = (f"Answer using ONLY the context below.\n\n"
              f"<context>\n{context}\n</context>\n\nQuestion: {user_q}")
    resp = client.messages.create(model=MODEL, max_tokens=200,
                                  messages=[{"role": "user", "content": prompt}])
    return resp.content[0].text
# THE EVAL SET: real inputs + the ground-truth fact each answer MUST contain.
# Anthropic's advice: start with 20-50 tasks drawn from real failures. Here are 4
# to see the shape; note the mix keeps it honest.
CASES = [
    {"q": "What is the refund policy?",     "must_contain": "30 days"},
    {"q": "How long does shipping take?",   "must_contain": "5-7"},
    {"q": "Tell me about the warranty.",    "must_contain": "1-year"},
    {"q": "Is express shipping available?", "must_contain": "2 days"},
]

# CODE-BASED GRADER: deterministic. No model judges the model here.
def grade(answer, must_contain):
    return must_contain.lower() in answer.lower()

passed = 0
for c in CASES:
    a  = rag_answer(c["q"])
    ok = grade(a, c["must_contain"])
    passed += ok
    print(f"[{'PASS' if ok else 'FAIL'}] {c['q']}  (need: {c['must_contain']!r})")

print(f"\nSCORE: {passed}/{len(CASES)} = {passed/len(CASES):.0%} accuracy")