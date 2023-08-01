from ai_translator.model import OpenAIModel, GLMModel
from ai_translator.utils import Config


class ModelFactory:
    @classmethod
    def create_model(cls, config:Config):
        if config.common.model_type == 'OpenAIModel':
            return OpenAIModel(model=config.OpenAIModel.model, api_key=config.OpenAIModel.api_key)
        elif config.common.model_type == 'GLMModel':
            return GLMModel(model_url=config.GLMModel.model_url, timeout=config.GLMModel.timeout)
