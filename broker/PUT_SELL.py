from global_vars import get_globals
from utilities.Print_Debug_Msg import print_debug_msg
from utilities.Check_Kotak_Positions import check_kotak_positions
from utilities.Get_Instrument_Quantity import get_instrument_qty
from broker.Close_Positions import close_positions
from recording.Post_Trans_Tasks import post_trans_tasks

settings = get_globals()

async def sell_put(signal):
    
    client = settings.get_neo_client()
    kotak_positions = client.positions()
    positions = check_kotak_positions(kotak_positions)
    put_positions = positions['PE']
    qty = 0
    instrument:str = settings._globals['nifty_put_instrument']
    
    existing_position:int = get_instrument_qty(put_positions,instrument)
    
    if signal['signal'] == "PE-T1" or signal['signal'] == "T1":
        qty:int = settings.data['nifty_default_lot_size'] * int(settings._globals['nifty_t1_lots'])
    else:
        qty:int = existing_position
    
    if qty > existing_position:
        return f"Can not sell as {instrument} position is : {existing_position} and sell qty is {qty}"
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
            tag=signal['tag']
            )
        
        if 'stat' not in order_result or order_result['stat'] != 'Ok':
            await close_positions(signal['option_type'])
            positions = check_kotak_positions(kotak_positions)
            print(f"Global PNL is : {settings.data['PNL']}")
            return True
            
        order_num = order_result['nOrdNo']
        order_report = client.order_history(order_id = order_num)
        
        order_report = order_report['data']
        if 'stat' not in order_report or order_report['stat'] != 'Ok':
            await close_positions(signal['option_type'])
            return True
            
        order_report = order_report['data']
        order_passed = not any(obj.get('ordSt') == 'rejected' for obj in order_report)
        if order_passed:
            recorded = await post_trans_tasks(signal,instrument, qty)
            return f"Order {signal['tag']} to SELL {instrument} : {qty} quantity IS PLACED."
        else:
            await close_positions(signal['option_type'])
            return True
            
    except Exception as e:
        await close_positions(signal['option_type'])
        print_debug_msg(e)