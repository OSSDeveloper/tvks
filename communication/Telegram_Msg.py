from global_vars import get_globals
settings = get_globals()

def get_telegram_msg_dict():
    msg_dict = {}
    msg_dict['header'] = "header"
    msg_dict['username'] = settings._globals['user']['name']
    msg_dict['context'] = "context"
    msg_dict['message'] = ""
    msg_dict['success'] = False
    return msg_dict