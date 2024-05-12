import builtins
from fastapi import FastAPI
from global_vars import GlobalSettings
from broker.Session import get_client
import rich
from rich.pretty import Pretty

builtins.print = rich.print

settings = GlobalSettings()

app = FastAPI()

get_client()

@app.get("/")
async def root():
    return {"message": settings._globals}
