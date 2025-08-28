from pathlib import Path

import yaml
from pydantic import BaseModel, Field


class ConfigPath:
    configs_folder = Path(__file__).parent.parent / 'env_configs'


class Config(BaseModel):
    url: str = Field(default=None)
    user_name: str = Field(default=None)
    password: str = Field(default=None)

    def load_config(self, env: str):
        env_config_path = ConfigPath.configs_folder / f'{env.lower()}.yaml'

        if env_config_path.is_file():
            with env_config_path.open('r') as file:
                env_data = yaml.safe_load(file)
            self.set_attrs(env_data)
            return self.model_validate(self)
        raise ValueError(f'Configuration file at {env_config_path} not exists')

    def set_attrs(self, data: dict):
        for key, value in data.items():
            if value:
                setattr(self, key, value)
        return self
