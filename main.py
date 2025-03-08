import utils.get_model as get_model
import chat_completions
import sys,os
from dotenv import load_dotenv

# model_lists = get_model.get_model_list()
# print(model_lists)

# for model_list in model_lists:
#     model_info = get_model.get_model_info(model_list)
#     print(model_info)

# content = "给我一条排查 linux 系统端口占用的命令。"

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import ArgumentParser

if __name__ == "__main__":
    argument_parser = ArgumentParser()
    args = argument_parser.parse_arguments()

    load_dotenv()
    openai_api_key = os.getenv('CHATGPT_API_KEY')

    model_name = args.openai_model if args.openai_model else "gpt-4o"