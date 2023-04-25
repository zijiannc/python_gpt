import threading
import openai
from model.model import chat_with_bot


openai.api_key = "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"


class WiseGroupChatController:
    def __init__(self, view):
        self.view = view
        self.temperature = 1.0
        self.message_history = []
        self.message_history.append({"role": "system", "content": "能否模拟一个由智囊团成员回答我的问题？智囊团包括乔布斯、\
比尔盖茨、蒂姆库克，苏格拉底和老子。请让他们以讨论的形式回答问题。\
请加入一个名为尼尔的新角色,他是28岁的中国人,任职于Zoetis的高级软件工程师,热爱动物,特别是猫和狗,希望建立与宠物相关的创业.\
请尽量详细地进行讨论。\
                                "})

        
    def send_message(self, user_message):
        self.view.display_user_message(user_message)

        if user_message.lower() == "quit":
            self.view.quit()
            return

        self.view.disable_input()

        threading.Thread(target=self.get_bot_response, args=("请智囊团来回答我的问题:" + user_message,)).start()

    def get_bot_response(self, user_message):
        bot_message = chat_with_bot(user_message, self.message_history,self.temperature)
        self.view.display_bot_message(bot_message)
        self.view.enable_input()
