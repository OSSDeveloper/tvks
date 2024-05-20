from global_vars import get_globals
import requests
import rich
import json 
settings = get_globals()
async def post_trans_tasks(signal, qty):
    url = 'https://asia-south1-nseoptiondata-408314.cloudfunctions.net/post_trans_tasks'
    
    data = {
        'tag': signal['tag'],
        'userid': settings._globals['user']['id'],
        'username': settings._globals['user']['name'],
        'strategy': signal['strategy'],
        'signal': signal['signal'],
        'option_type': signal['option_type'],
        'qty': qty,
        'ovalue': signal['ovalue']
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

# [SchemaField('tag', 'STRING', 'NULLABLE', None, None, (), None), SchemaField('userid', 'STRING', 'NULLABLE', None, None, (), None), SchemaField('username', 'STRING', 'NULLABLE', None, None, (), None), SchemaField('strategy', 'STRING', 'NULLABLE', None, None, (), None), SchemaField('signal', 'STRING', 'NULLABLE', None, None, (), None), SchemaField('option_type', 'STRING', 'NULLABLE', None, None, (), None), SchemaField('qty', 'INTEGER', 'NULLABLE', None, None, (), None), SchemaField('tdate', 'DATE', 'NULLABLE', "CURRENT_DATE('Asia/Kolkata')", None, (), None), SchemaField('ttime', 'TIME', 'NULLABLE', "CURRENT_TIME('Asia/Kolkata')", None, (), None), SchemaField('ovalue', 'NUMERIC(10, 2)', 'NULLABLE', None, None, (), None)]