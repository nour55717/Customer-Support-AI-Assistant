import chromadb
from chromadb.config import Settings

from app.core.config import CHROMA_DB_PATH
from app.core.logger import logger


class VectorStore:
    """
    Manage ChromaDB vector database.
    """

    def __init__(self):
        logger.info("Initializing ChromaDB...")

        self.client = chromadb.PersistentClient(
            path=str(CHROMA_DB_PATH),
            settings=Settings(
                anonymized_telemetry=False,
            ),
        )

        self.collection = self.client.get_or_create_collection(
            name="customer_support"
        )

        logger.info("ChromaDB initialized successfully.")

    def add_documents(
        self,
        ids,
        documents,
        embeddings,
        metadatas,
    ):
        """
        Add documents to ChromaDB in batches.
        """

        total_documents = len(documents)

        logger.info(
            f"Adding {total_documents} documents to ChromaDB..."
        )

        # ChromaDB maximum safe batch size
        batch_size = 5000

        total_batches = (
            total_documents + batch_size - 1
        ) // batch_size

        for batch_index, start in enumerate(
            range(0, total_documents, batch_size),
            start=1,
        ):

            end = min(start + batch_size, total_documents)

            self.collection.add(
                ids=ids[start:end],
                documents=documents[start:end],
                embeddings=embeddings[start:end].tolist(),
                metadatas=metadatas[start:end],
            )

            logger.info(
                f"Inserted batch {batch_index}/{total_batches} "
                f"({end}/{total_documents})"
            )

        logger.info("Documents added successfully.")