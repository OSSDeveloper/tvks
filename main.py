import builtins
import rich
builtins.print = rich.print

from global_vars import get_globals
from broker.Session import get_client

from fastapi import FastAPI, Request
from display_error import display_exception



get_client()

from broker.CALL_BUY import buy_call
from broker.CALL_SELL import sell_call

settings = get_globals()
client = settings.get_neo_client()


print(settings.data)

app = FastAPI()


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    display_exception(exc)

# @app.get("/")
# async def root():
#     return {"message": settings._globals['client']}

@app.post("/signal")
async def process_trade(trade_signal:Request):
    raw_signal = await trade_signal.json() if trade_signal.method == "POST" else {}

    signal = {}
    signal['trade_no'] = raw_signal.get('trade_no', None)
    signal['strategy'] = raw_signal.get('strategy', None)
    signal['action'] = raw_signal.get('action', None)
    signal['option_type'] = raw_signal.get('option_type', None)
    signal['ovalue'] = raw_signal.get('index', None)
    signal['signal'] = raw_signal.get('signal', None)
    signal['tag'] = str(signal['trade_no']) + "_" + str(signal['signal'])
        
    if signal['option_type'] == "CE" and signal['action'] == "BUY":
        result = await buy_call(signal)
        return result
    elif signal['option_type'] == "CE" and signal['action'] == "SELL":
        result = await sell_call(signal)
        return result
    return "There is some error in TV Parameters"