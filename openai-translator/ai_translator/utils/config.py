"""
安全：openai api key 默认从环境变量取
"""
import argparse
import os
from dataclasses import  dataclass

@dataclass
class OpenAIModelObj:
  model: str
  api_key: str

@dataclass
class GLMModelObj:
  model_url: str
  timeout: int

@dataclass
class CommonObj:
  book: str
  file_format: str
  model_type: str

@dataclass
class Config:
    OpenAIModel: OpenAIModelObj
    GLMModel: GLMModelObj
    common: CommonObj

    def __post_init__(self):
        self.OpenAIModel = OpenAIModelObj(**self.OpenAIModel)
        self.GLMModel = GLMModelObj(**self.GLMModel)
        self.common = CommonObj(**self.common)

        if len(self.OpenAIModel.api_key.replace('your_openai_api_key', '').strip()) < 1:
            self.OpenAIModel.api_key = os.getenv("OPENAI_API_KEY")
        if not self.common.model_type:
            self.common.model_type == 'OpenAIModel'
        elif self.common.model_type not in ['GLMModel', 'OpenAIModel']:
            raise Exception('Only support ai mode: GLMModel、OpenAIModel')


    def update(self, args:argparse.Namespace) -> None:
        """
        :param args: 命令行输入参数
        :return:
        """
        if args.model_type:
            self.common.model_type = args.model_type
        if args.glm_model_url:
            self.GLMModel.model_url = args.glm_model_url
        if args.timeout:
            self.GLMModel.timeout = args.timeout
        if args.openai_model:
            self.OpenAIModel.model = args.openai_model
        if args.openai_api_key:
            self.OpenAIModel.api_key = args.openai_api_key
        if args.book:
            self.common.book = args.book
        if args.file_format:
            self.common.file_format = args.file_format
