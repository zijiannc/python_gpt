import openai
openai.api_key = "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"

def chat_with_bot(user_message, message_history):
    message_history.append({"role": "user", "content": user_message})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.6,
        messages=message_history
    )

    bot_message = completion.choices[0].message.content
    message_history.append({"role": "assistant", "content": bot_message})
    return bot_message
