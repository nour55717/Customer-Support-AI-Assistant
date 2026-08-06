from app.services.chat_service import ChatService

chat = ChatService()

try:
    result = chat.ask("How can I cancel my order?")

    print("\n========== SUCCESS ==========\n")
    print(result)

except Exception as e:
    import traceback

    print("\n========== ERROR ==========\n")
    traceback.print_exc()