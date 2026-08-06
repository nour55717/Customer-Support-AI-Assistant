from app.rag.data_loader import CustomerSupportDataLoader
from app.rag.preprocessing import TextPreprocessor
from app.rag.embedding import EmbeddingModel


loader = CustomerSupportDataLoader()
df = loader.load_data()

preprocessor = TextPreprocessor()
df = preprocessor.preprocess_dataframe(df)

texts = (
    df["instruction"] + "\n\n" + df["response"]
).tolist()[:5]

model = EmbeddingModel()

embeddings = model.encode(texts)

print("Embedding Shape:", embeddings.shape)