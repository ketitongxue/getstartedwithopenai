import argparse

class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Translate English PDF book to Chinese.')
        self.parser.add_argument('--config', type=str, default='config.yaml', help='Configuration file with model and API settings.')
        self.parser.add_argument('--model_type', type=str, required=True, choices=['GLMModel', 'OpenAIModel'], help='The type of translation model to use. Choose between "GLMModel" and "OpenAIModel".')
        self.parser.add_argument('--openai_model', type=str, help='The model name of OpenAI Model. Required if model_type is "OpenAIModel".')
        # self.parser.add_argument('--openai_api_key', type=str, help='The API key for OpenAIModel. Required if model_type is "OpenAIModel".')

    def parse_arguments(self):
        args = self.parser.parse_args()
        # if args.model_type == 'OpenAIModel' and not args.openai_model and not args.openai_api_key:
        if args.model_type == 'OpenAIModel' and not args.openai_model:
            self.parser.error("--openai_model is required when using OpenAIModel")
        return args
