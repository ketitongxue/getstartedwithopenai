from openai import OpenAI
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

openai_api_key = os.getenv('CHATGPT_API_KEY')
# print(f"OPENAI_API_KEY={openai_api_key}")

client = OpenAI(
    api_key=openai_api_key,
)

# 生成文本
def get_completion():
    messages = [
        {
            "role": "system",
            "content": "你现在是一个运维专家，你的工作是帮助用户解决技术问题。",
        }
    ]

    while True:
        user_input = input("input Your Question:")
        if user_input == "quit":
            print("Bye~")
            break
        messages.append(
            {
                "role": "user",
                "content": user_input,
            }
        )

        print("当前聊天上下文：", messages)

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
        )

        reply = completion.choices[0].message.content
        print(f"\n运维专家: {reply}")

        messages.append(
            {
                "role": "assistant",
                "content": reply,
            }
        )