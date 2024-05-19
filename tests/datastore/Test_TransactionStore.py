import pytest
from datastore.TransasctionStore import TransactionStore

@pytest.fixture
def store():
    return TransactionStore()

def test_add_buy_transaction(store):
    store.add_transaction("msft", "CALL", "BUY", 10)
    assert store.get_open_positions()["CALL"]["MSFT"] == 10

def test_add_sell_transaction(store):
    store.add_transaction("msft", "CALL", "BUY", 10)
    store.add_transaction("msft", "CALL", "SELL", 5)
    assert store.get_open_positions()["CALL"]["MSFT"] == 5

def test_get_open_positions(store):
    store.add_transaction("msft", "CALL", "BUY", 10)
    store.add_transaction("msft", "PUT", "BUY", 20)
    open_positions = store.get_open_positions()
    assert open_positions == {"CALL": {"MSFT": 10}, "PUT": {"MSFT": 20}}

def test_has_open_position(store):
    store.add_transaction("msft", "CALL", "BUY", 10)
    assert store.has_open_position("CALL")

def test_no_open_position(store):
    assert not store.has_open_position("CALL")