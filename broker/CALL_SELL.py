from global_vars import get_globals
from utilities.Print_Debug_Msg import print_debug_msg
from utilities.Check_Kotak_Positions import check_kotak_positions
from utilities.Get_Instrument_Quantity import get_instrument_qty

settings = get_globals()


async def sell_call(signal):
    client = settings.get_neo_client()
    kotak_positions = client.positions()
    positions = check_kotak_positions(kotak_positions)
    call_positions = positions['CE']

    instrument:str = settings._globals['nifty_call_instrument']
    
    existing_position:int = get_instrument_qty(call_positions,instrument)
    
    if signal['signal'] == "CE-T1" or signal['signal'] == "T1":
        qty:int = settings['nifty_default_lot_size'] * int(settings._globals['nifty_t1_lots'])
    else:
        qty:int = existing_position
    
    if qty > existing_position:
        return f"Can not sell as {instrument} position is : {existing_position} and sell qty is {qty}"
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
            tag=signal['tag']
            )
        print_debug_msg(order_result)
        return order_result
    except Exception as e:
        print_debug_msg(e)