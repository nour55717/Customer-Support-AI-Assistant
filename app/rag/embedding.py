from sentence_transformers import SentenceTransformer
from typing import List

from app.core.config import EMBEDDING_MODEL
from app.core.logger import logger


class EmbeddingModel:
    """
    Generate embeddings using HuggingFace SentenceTransformer.
    """

    def __init__(self):
        logger.info(f"Loading embedding model: {EMBEDDING_MODEL}")
        self.model = SentenceTransformer(EMBEDDING_MODEL)
        logger.info("Embedding model loaded successfully.")

    def encode(self, texts: List[str]):
        """
        Convert list of texts to embedding vectors.
        """
        logger.info(f"Generating embeddings for {len(texts)} texts...")

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            show_progress_bar=True,
        )

        logger.info("Embeddings generated successfully.")

        return embeddings