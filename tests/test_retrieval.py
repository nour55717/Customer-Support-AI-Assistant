from app.rag.retrieval import Retriever

retriever = Retriever()

results = retriever.search(
    "How can I cancel my order?"
)

print("\n========== RESULTS ==========\n")

for doc in results["documents"][0]:
    print(doc)
    print("=" * 80)