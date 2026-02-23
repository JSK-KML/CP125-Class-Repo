import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise2.py')
_spec = importlib.util.spec_from_file_location("exercise2_lab7", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
withdraw = _module.withdraw


def test_valid_withdrawal():
    accounts = {"4111-1111": 500.00}
    assert withdraw(accounts, "4111-1111", 200.00) == 300.0

def test_exact_balance_withdrawal():
    accounts = {"4111-1111": 100.00}
    assert withdraw(accounts, "4111-1111", 100.00) == 0.0

def test_insufficient_funds():
    accounts = {"4222-2222": 80.00}
    assert withdraw(accounts, "4222-2222", 100.00) == "Insufficient Funds"

def test_card_not_found():
    accounts = {"4111-1111": 500.00}
    assert withdraw(accounts, "9999-0000", 50.00) == "Card Not Found"

def test_balance_updated_after_withdrawal():
    accounts = {"4111-1111": 500.00}
    withdraw(accounts, "4111-1111", 200.00)
    assert accounts["4111-1111"] == 300.0

def test_other_accounts_unaffected():
    accounts = {"4111-1111": 500.00, "4222-2222": 80.00}
    withdraw(accounts, "4111-1111", 100.00)
    assert accounts["4222-2222"] == 80.00

def test_zero_amount_withdrawal():
    accounts = {"4111-1111": 500.00}
    assert withdraw(accounts, "4111-1111", 0.00) == 500.0

def test_insufficient_funds_balance_unchanged():
    accounts = {"4222-2222": 50.00}
    withdraw(accounts, "4222-2222", 100.00)
    assert accounts["4222-2222"] == 50.00

def test_empty_accounts():
    accounts = {}
    assert withdraw(accounts, "4111-1111", 50.00) == "Card Not Found"

def test_sequential_withdrawals():
    accounts = {"4111-1111": 300.00}
    withdraw(accounts, "4111-1111", 100.00)
    result = withdraw(accounts, "4111-1111", 100.00)
    assert result == 100.0
