# import uvicorn
import builtins
import rich
builtins.print = rich.print

from global_vars import get_globals
from broker.Session import setup_neo_client

from fastapi import FastAPI, Request
from display_error import display_exception


print("WORKING TILL NOW - before setup_neo_client")
if setup_neo_client() == False:
    print("Unable to open connection with Kotak")
    exit(0)
print("WORKING TILL NOW - After setup_neo_client")
from broker.CALL_BUY import buy_call
from broker.CALL_SELL import sell_call
from broker.PUT_BUY import buy_put
from broker.PUT_SELL import sell_put
from utilities.Check_Kotak_Positions import check_kotak_positions
from utilities.PNL_Tasks import get_pnl
from utilities.IS_TIME_OK import is_time_ok

settings = get_globals()
client = settings.get_neo_client()

app = FastAPI()


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    display_exception(exc)

# @app.get("/")
# async def root():
#     return {"message": settings._globals['client']}
time_check = is_time_ok()
@app.post("/signal")
async def process_trade(trade_signal:Request):
    raw_signal = await trade_signal.json() if trade_signal.method == "POST" else {}

    print("-"*50)
    print("Got request with below params : ")
    print(raw_signal)
    
    signal = {}
    signal['trade_no'] = raw_signal.get('trade', None)
    signal['strategy'] = raw_signal.get('strategy', None)
    signal['action'] = raw_signal.get('action', None)
    signal['option_type'] = raw_signal.get('option_type', None)
    signal['ovalue'] = raw_signal.get('index', None)
    signal['signal'] = raw_signal.get('signal', None)
    signal['tag'] = str(signal['trade_no']) + "_" + str(signal['signal'])
        
    if signal['option_type'] == "CE" and signal['action'] == "BUY":
        result = await buy_call(signal)
        print_result(result)
        return result
    elif signal['option_type'] == "CE" and signal['action'] == "SELL":
        result = await sell_call(signal)
        print_result(result)
        return result
    elif signal['option_type'] == "PE" and signal['action'] == "BUY":
        result = await buy_put(signal)
        print_result(result)
        return result
    elif signal['option_type'] == "PE" and signal['action'] == "SELL":
        result = await sell_put(signal)
        print_result(result)
        return result
    
    return "There is some error in TV Parameters"

def print_result(result):
    print("Sending the below result back to requester :")
    print(result)
    pnl = get_pnl()

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
pnl = get_pnl()
print(f"Global limit is : {settings.data['LLIMIT']} to {settings.data['PLIMIT']} at the start...")