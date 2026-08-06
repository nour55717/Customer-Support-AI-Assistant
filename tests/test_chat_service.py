from app.services.chat_service import ChatService

chat = ChatService()

question = "How can I cancel my order?"

answer = chat.ask(question)

print("\n========== FINAL ANSWER ==========\n")
print(answer)