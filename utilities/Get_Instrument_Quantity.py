
def get_instrument_qty(data, instrument) -> int:
    instrument_dict = {d['instrument']: d['qty'] for d in data}
    return instrument_dict.get(instrument, 0)