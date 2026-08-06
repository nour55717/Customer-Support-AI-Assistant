from app.rag.data_loader import CustomerSupportDataLoader
from app.rag.preprocessing import TextPreprocessor
from app.rag.embedding import EmbeddingModel
from app.rag.vector_store import VectorStore
from app.rag.context_cleaner import ContextCleaner


print("Loading dataset...")

loader = CustomerSupportDataLoader()
df = loader.load_data()

print(f"Loaded {len(df)} records")

print("Preprocessing...")

preprocessor = TextPreprocessor()
df = preprocessor.preprocess_dataframe(df)

# Initialize Context Cleaner
context_cleaner = ContextCleaner()

documents = []
metadatas = []
ids = []

for index, row in df.iterrows():

    document = f"""
Customer Question:
{row["instruction"]}

Support Response:
{row["response"]}
"""

    # Clean placeholders before embedding
    document = context_cleaner.clean([document])[0]

    documents.append(document)

    metadatas.append(
        {
            "id": str(index),
            "category": row["category"],
            "intent": row["intent"],
            "flags": row["flags"],
            "instruction": row["instruction"],
        }
    )

    ids.append(str(index))

print(f"Building embeddings for {len(documents)} documents...")

embedding_model = EmbeddingModel()
embeddings = embedding_model.encode(documents)

vector_store = VectorStore()

try:
    vector_store.client.delete_collection("customer_support")
    print("Old collection deleted.")
except Exception:
    print("No previous collection found.")

vector_store.collection = vector_store.client.get_or_create_collection(
    name="customer_support"
)

vector_store.add_documents(
    ids=ids,
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas,
)

print(f"\n✅ Vector Database Rebuilt Successfully ({len(documents)} documents)")