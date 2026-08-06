from app.rag.embedding import EmbeddingModel
from app.rag.vector_store import VectorStore
from app.core.logger import logger


class Retriever:
    """
    Retrieve similar documents from ChromaDB.
    """

    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.vector_store = VectorStore()

    def search(self, query: str, top_k: int = 5):

        logger.info(f"Searching for: {query}")

        query_embedding = self.embedding_model.encode([query])[0]

        results = self.vector_store.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=top_k,
            include=[
                "documents",
                "metadatas",
                "distances",
            ],
        )

        logger.info(
            f"Retrieved {len(results['documents'][0])} documents."
        )

        return {
            "documents": results["documents"][0],
            "distances": results["distances"][0],
            "metadatas": results["metadatas"][0],
        }