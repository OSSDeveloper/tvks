from sys import exception
from neo_api_client import NeoAPI
import rich, builtins
from global_vars import get_globals
from display_error import display_exception
builtins.print = rich.print
settings = get_globals()

def setup_neo_client():
    print("WORKING TILL NOW - start line of setup_neo_client")
    print(settings._globals['mobile'])
    print(settings._globals['password'])
    print(settings._globals['consumer_key'])
    print(settings._globals['consumer_secret'])
    try:
        # utilities = settings._globals['utilities']
        # utilities.print_debug_msg("Started get client function execution")
        client = NeoAPI(
            consumer_key = settings._globals['consumer_key'],
            consumer_secret = settings._globals['consumer_secret'],
            neo_fin_key="neotradeapi",
            environment='prod',
        )
        print("Client is : ")
        
        print("WORKING TILL NOW - inside setup_neo_client")
        login_result = client.login(mobilenumber=settings._globals['mobile'], password=settings._globals['password'])
        
        print("STEP 1 : Login done")
        session_result = client.session_2fa(OTP=settings._globals['mpin'])
        print("STEP 2 : Session done")
        client.on_message = on_message  # called when message is received from websocket
        client.on_error = on_error  # called when any error or exception occurs in code or websocket
        client.on_close = on_close  # called when websocket connection is closed
        client.on_open = on_open  # called when websocket successfully connects
        print("\n \n ------------------------------------------------------------------------------ \n \n")
        
        settings._globals['user'] = {}
        settings._globals['user']['id'] = session_result['data']['ucc']
        settings._globals['user']['name'] = session_result['data']['greetingName']
        print(settings._globals['user'])
        settings.assign_neo_client(client)

        print("--------------------------------- \n\n\n")
        print("Broker client setup DONE.")
        print("\n\n\n ---------------------------------")

        return True
    except Exception as e:
        rich.print("Came to exception in opening kotak session")
        display_exception(e)
        return False


def on_message(message):
    print(message)
    
def on_error(error_message):
    print(error_message)

def on_close(message):
    print(message)
    
def on_open(message):
    print(message)