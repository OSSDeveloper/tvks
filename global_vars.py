from pydantic_settings import BaseSettings
from dotenv import load_dotenv, dotenv_values
import os


class GlobalSettings(BaseSettings):
    company: str = "Process Bricks Technologies"
    _globals: dict = {}
    

    class Config:
        env_file = ".env"
        extra = "allow"


    def __init__(self, **values):
        super().__init__(**values)
        load_dotenv()
        # self._globals = {k: v for k, v in os.environ.items() if k not in self.__class__.model_fields}
        self._globals = dotenv_values(".env")