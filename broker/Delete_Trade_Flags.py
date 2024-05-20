
from global_vars import get_globals
settings = get_globals()

def Get_Trade_Flag(option_type):
    if option_type == 'CE':
        return settings.data['call_trade_flag']
    elif option_type == 'PE':
        return settings.data['put_trade_flag']
    return False

def Set_Trade_Flag(option_type, value):
    if option_type == 'CE':
        settings.data['call_trade_flag'] = value
    elif option_type == 'PE':
        settings.data['put_trade_flag'] = value