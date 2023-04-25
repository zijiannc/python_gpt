import threading
import openai
from model.model import chat_with_bot


openai.api_key = "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"


class NaNa_ChatController:
    def __init__(self, view):
        self.view = view
        self.message_history = []
        self.message_history.append({"role": "system", "content": "对于这个聊天的一些基本信息：\
                                我的名字: NaNa\
                                我的年龄: 5岁\
                                我的主人: Neal\
                                "})

        
    def send_message(self, user_message):
        self.view.display_user_message(user_message)

        if user_message.lower() == "quit":
            self.view.quit()
            return

        self.view.disable_input()

        threading.Thread(target=self.get_bot_response, args=(user_message,)).start()

    def get_bot_response(self, user_message):
        bot_message = chat_with_bot(user_message, self.message_history)
        self.view.display_bot_message(bot_message)
        self.view.enable_input()
