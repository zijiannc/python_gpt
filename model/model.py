import openai
import concurrent.futures

openai.api_key = "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"
openai.api_key = "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"
def chat_with_bot(user_message, message_history, customize_temperature=0.6, timeout_seconds=60):
    message_history.append({"role": "user", "content": user_message})

    def create_completion():
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=customize_temperature,
            messages=message_history
        )
        bot_message = completion.choices[0].message.content
        message_history.append({"role": "assistant", "content": bot_message})
        return bot_message

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(create_completion)
        try:
            bot_message = future.result(timeout=timeout_seconds)
            return bot_message
        except concurrent.futures.TimeoutError:
            return "请求超时，请重试。"
