from utilities.Get_Pnl import get_pnl

def check_kotak_positions(obj):
    positions = {'CE': [], 'PE':[]}

    # if obj is not None:
    #     PNL = get_pnl(obj)
    
    if 'stat' not in obj or obj['stat'] != 'Ok':
        return positions
    
    for instrument in obj['data']:
        position = {}
        buy_qty = int(instrument['cfBuyQty']) + int(instrument['flBuyQty'])
        sell_qty = int(instrument['cfSellQty']) + int(instrument['flSellQty'])
        total_qty = buy_qty - sell_qty
        if total_qty > 0:
            position['instrument'] = instrument['trdSym']
            position['qty'] = total_qty
            option_type = instrument['trdSym'][-2:]
            positions[option_type].append(position)
    return positions