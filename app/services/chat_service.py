from app.core.logger import logger
from app.rag.llm import GeminiLLM
from app.rag.prompt_builder import PromptBuilder
from app.rag.retrieval import Retriever
from app.rag.context_cleaner import ContextCleaner
from app.services.conversation import ConversationMemory


class ChatService:
    """
    Complete RAG Chat Service with Conversation Memory.
    """

    def __init__(self):
        logger.info("Initializing Chat Service...")

        self.retriever = Retriever()
        self.prompt_builder = PromptBuilder()
        self.context_cleaner = ContextCleaner()
        self.memory = ConversationMemory()
        self.llm = GeminiLLM()

        logger.info("Chat Service initialized successfully.")

    def ask(self, question: str):

        logger.info(f"User Question: {question}")

        try:

            # Save user message
            self.memory.add_user_message(question)

            # Retrieve similar documents
            results = self.retriever.search(question)

            documents = results["documents"]
            distances = results["distances"]
            metadatas = results["metadatas"]

            # Clean retrieved documents
            documents = self.context_cleaner.clean(documents)

            # Conversation history
            history = self.memory.get_history()

            # Build prompt
            prompt = self.prompt_builder.build(
                question=question,
                documents=documents,
                history=history,
            )

            # Generate answer
            answer = self.llm.generate(prompt)

            # Clean generated answer
            answer = self.context_cleaner.clean([answer])[0]

            # Save assistant response
            self.memory.add_assistant_message(answer)

            # Confidence score (average of top 3 results)
            if distances:

                top_distances = distances[:3]

                confidence = round(
                    sum(
                        100 / (1 + d)
                        for d in top_distances
                    ) / len(top_distances),
                    2,
                )

            else:

                confidence = 0.0

            # Format retrieved sources
            formatted_sources = []

            for metadata, distance in zip(metadatas, distances):

                similarity = round(
                    (100 / (1 + distance)),
                    2,
                )

                category = (
                    metadata.get("category", "Unknown")
                    .replace("_", " ")
                    .title()
                )

                intent = (
                    metadata.get("intent", "Unknown")
                    .replace("_", " ")
                    .title()
                )

                question_text = self.context_cleaner.clean(
                    [
                        metadata.get(
                            "instruction",
                            "",
                        )
                    ]
                )[0]

                formatted_sources.append(
                    {
                        "category": category,
                        "intent": intent,
                        "question": question_text,
                        "similarity": similarity,
                    }
                )

            return {
                "answer": answer,
                "confidence": confidence,
                "sources": formatted_sources[:3],
            }

        except Exception:

            logger.exception("ChatService Error")

            raise