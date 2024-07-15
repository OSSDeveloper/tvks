from global_vars import get_globals
from utilities.Print_Debug_Msg import print_debug_msg
settings = get_globals()

def get_nifty_instrument(index_value, option_type):
    nifty_strike_interval = settings.data['nifty_strike_interval']
    deviation = settings.data['deviation']
    ITM_distance = nifty_strike_interval * deviation
    otc = ""
    try:
        nearest_strike = round(index_value / nifty_strike_interval) * nifty_strike_interval
        if option_type == "CE":
            strike = nearest_strike - ITM_distance
            otc = "C"
        else:
            strike = nearest_strike + ITM_distance
            otc = "P"

    except Exception as e:
        print(e)
        return None