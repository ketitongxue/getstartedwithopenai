from openai import OpenAI
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

class GetModel:
    def __init__(self):
        self.openai_api_key = os.getenv('CHATGPT_API_KEY')        

    # 获取 OPENAI 模型列表
    def get_model_list(self):
        client = OpenAI(
            api_key = self.openai_api_key,
        )
        # print(f"models_list:{client.models.list()}")
        # print(type(client.models.list()))

        models = client.models.list()

        model_list = []
        for model in models:
            # print(model.id)  # 访问模型的id
            model_list.append(model.id)
            # print(model.owned_by)  # 访问模型的所有者
            # print(model.created)  # 创建时间
        return model_list

    # 获取 OPENAI 模型的具体信息
    def get_model_info(self, model):
        client = OpenAI(
            api_key = self.openai_api_key,
        )
        model_info = client.models.retrieve(model)

        # print(model_info)
        return model_info
