from app.rag.retrieval import Retriever
from app.rag.prompt_builder import PromptBuilder


retriever = Retriever()

results = retriever.search(
    "How can I cancel my order?"
)

documents = results["documents"][0]

builder = PromptBuilder()

prompt = builder.build(
    "How can I cancel my order?",
    documents,
)

print(prompt)