import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import ArgumentParser, ConfigLoader, LOG, Config
from model import GLMModel, OpenAIModel
from translator import PDFTranslator
from utils.mode_creator import  ModelFactory

if __name__ == "__main__":
    argument_parser = ArgumentParser()
    args = argument_parser.parse_arguments()
    config_loader = ConfigLoader(args.config)

    config = config_loader.load_config()
    config.update(args)

    model = ModelFactory.create_model(config)

    # 实例化 PDFTranslator 类，并调用 translate_pdf() 方法
    translator = PDFTranslator(model)
    translator.translate_pdf(config.common.book, config.common.file_format)
