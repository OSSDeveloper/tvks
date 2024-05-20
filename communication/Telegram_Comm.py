from telegram import Bot
from telegram.constants import ParseMode
from utilities.Print_Debug_Msg import print_debug_msg

from global_vars import get_globals
settings = get_globals()
class Tele_Bot:
    def __init__(self):
        self.USER = settings._globals['user']['name']
        self.CRED_PATH = ""
        self.bot = Bot(settings._globals['telegram_token'])

    async def send_telegram_msg(self, obj_msg):
        try:
            msg = self.parse_telegram_markdown(obj_msg)
            msg_sent = await self.bot.send_message(chat_id=settings._globals['telegram_trade_group_chat_id'], text=msg,  parse_mode=ParseMode.MARKDOWN)
            return True
        except Exception as e:
            print_debug_msg(e)
            print(msg)
            return False

    def parse_telegram_markdown(self, obj_msg):
        try:
            parsed_message = ''
            if obj_msg.get('header', 'Transaction'):
                parsed_message += f'**{obj_msg["header"]}**\n'
            if obj_msg.get('username', "PB"):
                parsed_message += f'@{obj_msg["username"]}\n'
            parsed_message += f'{obj_msg.get("context", "Transaction Success")}\n'
            parsed_message += obj_msg.get('message', '')

            if obj_msg.get('success',False):
                parsed_message = chr(0x1F49A) + ' ' + parsed_message 
            else:
                parsed_message = chr(0x2764) + ' ' + parsed_message
            
            return parsed_message
        except Exception as e:
            print_debug_msg(e)
            return f"ERROR WHILE PARSING TELEGRAM MESSAGE. \n\n msg input is : \n\n {str(obj_msg)}"