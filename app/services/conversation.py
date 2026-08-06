from collections import deque


class ConversationMemory:
    """
    Store conversation history for the current session.
    """

    def __init__(self, max_messages: int = 6):
        self.history = deque(maxlen=max_messages)

    def add_user_message(self, message: str):
        self.history.append(
            {
                "role": "user",
                "content": message,
            }
        )

    def add_assistant_message(self, message: str):
        self.history.append(
            {
                "role": "assistant",
                "content": message,
            }
        )

    def get_history(self):
        return list(self.history)

    def clear(self):
        self.history.clear()