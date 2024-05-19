from typing import Any
from pydantic_settings import BaseSettings
from dotenv import load_dotenv, dotenv_values
import os
from neo_api_client import NeoAPI
from utilities import All_Utilities

class GlobalSettings(BaseSettings):
    company: str = "Test Legal Entity"
    _globals: dict = {}
    data: dict = {}
    
    client: Any = None
    class Config:
        env_file = ".env"
        extra = "allow"

    def assign_neo_client(self, client):
        print("-------------- Client about to be assigned globally ------------------------")
        self.client = client
        print (self.get_neo_client())
        print("----------------------- Client Global Assignment completed ---------------")

    def get_neo_client(self):
        return self.client

    def __init__(self, **values):
        super().__init__(**values)
        load_dotenv()
        # self._globals = {k: v for k, v in os.environ.items() if k not in self.__class__.model_fields}
        self._globals = dotenv_values(".env")
        
        self.data['nifty_default_lot_size'] = 25
        self.data['exchange_segment'] = "nse_fo"
        self.data['product'] = "MIS"
        self.data['order_type'] = "MKT"
        self.data['validity'] = "IOC"
        self.data['amo'] = "NO"
        self.data['pf'] = "N"

    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value

    def __iter__(self):
        for item in self.data:
            yield item

settings = GlobalSettings()

def get_globals():
    return settings