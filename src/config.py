import json
from typing import List


class Config:
    def __init__(self, path: str):
        self.path = path
        self.config = self.load_config()

    def load_config(self) -> object:
        """
        Load config from json file

        :return:
        """
        with open(self.path, 'r') as f:
            config = json.load(f)
        return config

    def get(self, key: str | List[str]):
        """
        Get config value by key

        :param key: the key, or list of keys wanted to access
        :return: config value
        """
        if not isinstance(key, list):
            return self.config[key]

        accessed_config = self.config

        for k in key:
            accessed_config = accessed_config[k]

        return accessed_config