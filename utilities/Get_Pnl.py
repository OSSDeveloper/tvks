from datetime import datetime


def get_pnl(positions):
    
    PNL = 0
    from global_vars import get_globals
    settings = get_globals()
    
    if 'stat' not in positions or positions['stat'] != 'Ok':
        print(f"P&L is {PNL}.")
        return PNL

    for trade in positions['data']:
        # cfBuyQty = float(trade.get('cfBuyQty',0)) / float(trade.get('lotSz',1))
        # flBuyQty = float(trade.get('flBuyQty',0)) / float(trade.get('lotSz',1))
        # cfSellQty = float(trade.get('cfSellQty',0)) / float(trade.get('lotSz',1))
        # flSellQty = float(trade.get('flSellQty',0)) / float(trade.get('lotSz',1))
        # buy_qty = cfBuyQty + flBuyQty
        # sell_qty = cfSellQty + flSellQty
        # net_qty = buy_qty - sell_qty
        
        cfBuyAmt = float(trade.get('cfBuyAmt', 0))
        buyAmt = float(trade.get('buyAmt',0))
        cfSellAmt  = float(trade.get('cfSellAmt',0))
        sellAmt = float(trade.get('sellAmt',0))
        buy_amount = cfBuyAmt + buyAmt
        sell_amount = cfSellAmt + sellAmt
        PNL = float(PNL) + float((sell_amount - buy_amount))
        
    settings.data['PNL'] = PNL
    print(f"P&L is {PNL}.")
    return PNL