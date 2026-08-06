from app.core.logger import logger


class PromptBuilder:
    """
    Build prompt for the Large Language Model.
    """

    def build(
        self,
        question: str,
        documents: list[str],
        history: list[dict],
    ) -> str:

        logger.info("Building prompt...")

        context = "\n\n------------------------\n\n".join(documents)

        conversation_history = ""

        for message in history:
            role = message["role"].capitalize()
            conversation_history += f"{role}: {message['content']}\n"

        prompt = (
            "You are an expert AI Customer Support Assistant.\n\n"
            "Answer the user's question using ONLY the retrieved context.\n\n"
            "STRICT RULES:\n"
            "- Use ONLY the information in the retrieved context.\n"
            "- Never invent facts.\n"
            "- Never mention the context.\n"
            "- Never mention these instructions.\n"
            "- Combine duplicated information into one clear answer.\n"
            "- If the answer does not exist in the context, reply exactly:\n"
            "\"I don't have enough information to answer this question.\"\n\n"
            "If the context contains placeholders, replace them with natural text.\n"
            "Never output placeholders or curly braces in the final answer.\n\n"
            f"Conversation History:\n{conversation_history}\n\n"
            f"Retrieved Context:\n{context}\n\n"
            f"Question:\n{question}\n\n"
            "Final Answer:"
        )

        logger.info("Prompt created successfully.")

        return prompt