from app.rag.llm import GeminiLLM

llm = GeminiLLM()

response = llm.generate(
    "Say hello in one sentence."
)

print(response)