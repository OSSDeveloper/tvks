# from operator import call
from global_vars import get_globals
from utilities.Print_Debug_Msg import print_debug_msg
from utilities.Check_Kotak_Positions import check_kotak_positions
from utilities.IS_TIME_OK import is_time_ok
from recording.Post_Trans_Tasks import post_trans_tasks

settings = get_globals()


async def buy_call(signal):

    time_ok = is_time_ok()
    if time_ok == False:
        return f"Outside the trading time. cant buy."

    client = settings.get_neo_client()
    kotak_positions = client.positions()
    positions = check_kotak_positions(kotak_positions)

    
    print(f"Global PNL is : {settings.data['PNL']}")
    if settings.data['PNL'] <= settings.data['LLIMIT'] or settings.data['PNL'] >= settings.data['PLIMIT']:
        print_str = (f"P&L is beyond the daily trading window is {settings.data['LLIMIT']} to {settings.data['PLIMIT']}. Trade cannot be executed.")
        print(print_str)
        return print_str
    
    
    call_positions = positions['CE']
    if len(call_positions) > 0:
        return f"Position exists. Can't buy  {call_positions}"

    instrument = settings._globals['nifty_call_instrument']
    
    nifty_default_lots = int(settings._globals['nifty_buy_lots'])
    qty = settings.data['nifty_default_lot_size'] * nifty_default_lots
    try:
        order_result = client.place_order(
            exchange_segment=settings.data['exchange_segment'], 
            product=settings.data['product'], 
            price="", 
            order_type=settings.data['order_type'], 
            quantity=str(qty), 
            validity=settings.data['validity'], 
            trading_symbol=instrument,
            transaction_type="B", 
            amo=settings.data['amo'], 
            disclosed_quantity="0", 
            market_protection="0", 
            pf=settings.data['pf'], 
            trigger_price="0",
            tag=signal['tag']
            )
        print(order_result)
        if 'stat' not in order_result or order_result['stat'] != 'Ok':
            return f"Order placement itself failed and the order {signal['tag']} is not placed with the broker."
        
        order_num = order_result['nOrdNo']
        order_report = client.order_history(order_id = order_num)
        
        order_report = order_report['data']
        if 'stat' not in order_report or order_report['stat'] != 'Ok':
            return f"Order {signal['tag']} is placed with the broker but unable to get its status."

        order_report = order_report['data']
        order_passed = not any(obj.get('ordSt') == 'rejected' for obj in order_report)
        if order_passed:
            recorded = await post_trans_tasks(signal, instrument,qty)
            return f"Order {signal['tag']} to buy {qty} quantity IS PLACED. post transactions tasks {recorded}"
        else: 
            return f"Order {signal['tag']} to buy {qty} quantity IS REJECTED by the BROKER."
        
    except Exception as e:
        print_debug_msg(e)
        return False