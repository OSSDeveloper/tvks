from global_vars import get_globals
from utilities.Print_Debug_Msg import print_debug_msg
settings = get_globals()
from datetime import datetime, time
import pytz
timezone='Asia/Kolkata'
ist = pytz.timezone(timezone)
from_time_str = settings.data['start_time']
to_time_str = settings.data['end_time']
def is_time_ok():
    from_time = datetime.strptime(from_time_str, "%H:%M").time()
    to_time = datetime.strptime(to_time_str, "%H:%M").time()
    current_time = datetime.now(ist).time()
    print(f"From time: {from_time} - current time : {current_time} - to time : {to_time}.")
    print(from_time <= current_time <= to_time)
    return from_time <= current_time <= to_time
    