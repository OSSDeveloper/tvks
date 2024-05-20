from global_vars import get_globals
from utilities.Print_Debug_Msg import print_debug_msg
from utilities.Check_Kotak_Positions import check_kotak_positions
from utilities.Get_Instrument_Quantity import get_instrument_qty

from recording.Post_Trans_Tasks import post_trans_tasks
import asyncio

settings = get_globals()

client = settings.get_neo_client()

async def close_positions(option_type):
    while True:
        # Try to close trades
        await sell_positions(option_type)
        #Check again for positions
        qty = await get_quantity(option_type)
        
        if qty is not None:
            if qty == 0:
                return True
            else:
                await asyncio.sleep(settings['sleep_interval'])
        else:
            await asyncio.sleep(settings['sleep_interval'])

async def sell_positions(option_type):
    
    qty = await get_quantity(option_type)

    if qty is None:
        return False
    
    if qty == 0:
        print(f"Position for the instrument {instrument} is 0")
        return True
    
    
    if option_type == "CE":
        instrument:str = settings._globals['nifty_call_instrument']
    else:
        instrument:str = settings._globals['nifty_put_instrument']

    try:
        order_result = client.place_order(
            exchange_segment=settings['exchange_segment'], 
            product=settings['product'], 
            price="", 
            order_type=settings['order_type'], 
            quantity=str(qty), 
            validity=settings['validity'], 
            trading_symbol=instrument,
            transaction_type="S", 
            amo=settings['amo'], 
            disclosed_quantity="0", 
            market_protection="0", 
            pf=settings['pf'], 
            trigger_price="0",
            tag=""
            )
        return True
    except Exception as e:
        print_debug_msg(e)
        return False


async def get_quantity(option_type):
    try:
        
        kotak_positions = client.positions()
        positions = check_kotak_positions(kotak_positions)
        positions = positions[option_type]
        
        if option_type == "CE":
            instrument:str = settings._globals['nifty_call_instrument']
        else:
            instrument:str = settings._globals['nifty_put_instrument']

        existing_position:int = get_instrument_qty(positions,instrument)
        qty:int = existing_position
        return qty
    except Exception as e:
        print_debug_msg(e)
        return None