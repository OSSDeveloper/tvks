import builtins
import rich
builtins.print = rich.print

from global_vars import get_globals
from utilities.Check_Kotak_Positions import check_kotak_positions

settings = get_globals()
client = settings.get_neo_client()

def get_pnl():
    success = update_PNL()
    pnl = settings.data['PNL']
    print(f"Global PNL is : {pnl}")
    print("-"*60)
    print(" ")
    return pnl

def update_PNL():
    kotak_positions = client.positions()
    positions = check_kotak_positions(kotak_positions)
    return True
    

