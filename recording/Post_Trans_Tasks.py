from global_vars import get_globals
from communication.Telegram_Comm import Tele_Bot
import requests
import rich
import json 
import builtins

builtins.print = rich.print
settings = get_globals()
tele_bot = Tele_Bot()

async def post_trans_tasks(signal, instrument, qty):
    try:
        url = settings._globals['recording_url']
        data = {
            'tag': signal['tag'],
            'userid': settings._globals['user']['id'],
            'username': settings._globals['user']['name'],
            'strategy': signal['strategy'],
            'signal': signal['signal'],
            'option_type': signal['option_type'],
            'qty': qty,
            'ovalue': signal['ovalue'],
            'instrument': instrument
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json.dumps(data), headers=headers)
        if response.status_code == 200:
            print('Cloud Function executed successfully')
            return True
        else:
            print('Error calling Cloud Function:', response.text)
            return False
    except Exception as e:
        print('Error:', e)
        return False


# result = post_trans_tasks(
#     "test","v","b","st","CE-ENTRY","CE",50,89.65
# )

# rich.print(result)
