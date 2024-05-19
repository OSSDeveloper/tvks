from datetime import datetime
class Trade_Record:
    def __init__(self, userid, username, strategy, instrument, signal, quantity, value):
        self.record = {
            'date': datetime.today().strftime("%Y-%m-%d"),
            'time': datetime.today().strftime("%H:%M:%S"),
            'userid': userid,
            'username': username,
            'strategy': strategy,
            'instrument': instrument,
            'signal': signal,
            'quantity': quantity,
            'value': value
        }

    def get_trade_record(self):
        return self.record