import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()
MODEL = "claude-haiku-4-5"   # cheap for practice; identical on opus

# A tiny "knowledge base." Real RAG stores these as embeddings in a vector DB and
# retrieves by semantic similarity; we use a dict + keyword match so the DATA FLOW
# stays visible instead of buried in a library.
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

user_q = "What is your refund policy?"
doc_id, context = retrieve(user_q)          # RETRIEVE
print("retrieved:", doc_id)

# AUGMENT: paste the retrieved chunk into the prompt as grounding
prompt = (f"Answer using ONLY the context below.\n\n"
          f"<context source=\"{doc_id}\">\n{context}\n</context>\n\n"
          f"Question: {user_q}")

resp = client.messages.create(model=MODEL, max_tokens=300,      # GENERATE
                              messages=[{"role": "user", "content": prompt}])
print("answer:", resp.content[0].text)