class TransactionStore:
    def __init__(self):
        self.open_positions = {"CALL": {}, "PUT": {}}

    def _add_position(self, instrument, option_type, quantity):
        if instrument.upper() in self.open_positions[option_type]:
            self.open_positions[option_type][instrument.upper()] += quantity
        else:
            self.open_positions[option_type][instrument.upper()] = quantity

    def _remove_position(self, instrument, option_type, quantity):
        if instrument.upper() in self.open_positions[option_type]:
            self.open_positions[option_type][instrument.upper()] -= quantity
            if self.open_positions[option_type][instrument.upper()] <= 0:
                del self.open_positions[option_type][instrument.upper()]

    def add_transaction(self, instrument, option_type, transaction_type, quantity):
        instrument = instrument.upper()
        option_type = option_type.upper()
        transaction_type = transaction_type.upper()
        if transaction_type == "BUY":
            self._add_position(instrument, option_type, quantity)
        elif transaction_type == "SELL":
            self._remove_position(instrument, option_type, quantity)

    def get_open_positions(self):
        return self.open_positions

    def has_open_position(self, option_type):
        return bool(self.open_positions[option_type])