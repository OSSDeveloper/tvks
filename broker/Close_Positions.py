from global_vars import get_globals
from utilities.Print_Debug_Msg import print_debug_msg
from utilities.Check_Kotak_Positions import check_kotak_positions
from utilities.Get_Instrument_Quantity import get_instrument_qty
from communication.Telegram_Comm import Tele_Bot
from communication.Telegram_Msg import get_telegram_msg_dict
from recording.Post_Trans_Tasks import post_trans_tasks
import asyncio

settings = get_globals()

client = settings.get_neo_client()
tele_bot = Tele_Bot()

async def close_positions(option_type):
    msg_dict = get_telegram_msg_dict()
    msg_dict['header'] = "Closing Positions"
    msg_dict['message'] = f"Closing {option_type} positions"
    msg_sent = await tele_bot.send_telegram_msg(msg_dict)
    while True:
        # Try to close trades
        await sell_positions(option_type)
        #Check again for positions
        qty = await get_quantity(option_type)
        
        if qty is not None:
            if qty == 0:
                msg_dict['header'] = "POSITIONS CLOSED"
                msg_dict['message'] = f"All {option_type} positions are closed."
                msg_dict['success'] = True
                msg_sent = await tele_bot.send_telegram_msg(msg_dict)
                return True
            else:
                await asyncio.sleep(settings['sleep_interval'])
        else:
            await asyncio.sleep(settings['sleep_interval'])

async def sell_positions(option_type):
    
    qty = await get_quantity(option_type)

    if qty is None:
        return False

    if option_type == "CE":
        instrument:str = settings._globals['nifty_call_instrument']
    else:
        instrument:str = settings._globals['nifty_put_instrument']
    
    if qty == 0:
        print(f"Position for the instrument {instrument} is 0")
        return True

    try:
        order_result = client.place_order(
            exchange_segment=settings.data['exchange_segment'], 
            product=settings.data['product'], 
            price="", 
            order_type=settings.data['order_type'], 
            quantity=str(qty), 
            validity=settings.data['validity'], 
            trading_symbol=instrument,
            transaction_type="S", 
            amo=settings.data['amo'], 
            disclosed_quantity="0", 
            market_protection="0", 
            pf=settings.data['pf'], 
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