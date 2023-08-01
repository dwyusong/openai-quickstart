import yaml

from .config import Config


class ConfigLoader:
    def __init__(self, config_path):
        self.config_path = config_path

    def load_config(self):
        with open(self.config_path, "r") as f:
            config = yaml.safe_load(f)
            config_obj = Config(**config)
            return config_obj
