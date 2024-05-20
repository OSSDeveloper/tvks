from global_vars import get_globals
import requests
import rich
import json 
settings = get_globals()
async def post_trans_tasks(signal, instrument, qty):
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

# result = post_trans_tasks(
#     "test","v","b","st","CE-ENTRY","CE",50,89.65
# )

# rich.print(result)
