from model.model import chat_with_bot

def main():
    message_history = []
    message_history.append({"role": "system", "content": "对于这个聊天的一些基本信息：\
                            我的名字: NaNa\
                            我的年龄: 5岁\
                            我的主人: Neal\
                            "})

    print("Welcome to the chatbot! Type 'quit' to exit.")
    
    while True:
        user_message = input("You: ")

        if user_message.lower() == "quit":
            break

        bot_message = chat_with_bot(user_message, message_history)
        print(f"Bot: {bot_message}")

if __name__ == "__main__":
    main()
