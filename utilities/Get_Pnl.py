from datetime import datetime


def get_pnl(positions):
    
    PNL = 0
    from global_vars import get_globals
    settings = get_globals()
    
    if 'stat' not in positions or positions['stat'] != 'Ok':
        # current_time = datetime.now()
        # time_part = current_time.strftime("%I:%M:%S %p")
        # # print("type of time_part is : ",type(time_part))
        # print("Time part is : ", time_part)
        print(f"P&L is {PNL}.")
        return PNL

    for trade in positions['data']:
        cfBuyAmt = float(trade.get('cfBuyAmt', 0))
        buyAmt = float(trade.get('buyAmt',0))
        cfSellAmt  = float(trade.get('cfSellAmt',0))
        sellAmt = float(trade.get('sellAmt',0))
        buy_amount = cfBuyAmt + buyAmt
        sell_amount = cfSellAmt + sellAmt
        print(buy_amount)
        print(sell_amount)
        PNL = float(PNL) + float((sell_amount - buy_amount))
        
    settings.data['PNL'] = PNL
    # current_time = datetime.now()
    # time_part = current_time.strftime("%I:%M:%S %p")
    # print("Time is : ", time_part)
    print(f"P&L is {PNL}.")
    return PNL