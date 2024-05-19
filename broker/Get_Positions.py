from global_vars import get_globals
settings = get_globals()
client = settings.get_neo_client()

def get_Positions():
    positions = client.positions()