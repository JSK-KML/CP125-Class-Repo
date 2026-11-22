
import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise11 import is_valid_multiple, is_balance_sufficient, process_withdrawal

def test_is_valid_multiple():
    assert is_valid_multiple(10) == True
    assert is_valid_multiple(20) == True
    assert is_valid_multiple(50) == True
    assert is_valid_multiple(5) == False
    assert is_valid_multiple(101) == False
    assert is_valid_multiple(0) == False
    assert is_valid_multiple(-10) == False

def test_is_balance_sufficient():
    assert is_balance_sufficient(100, 100) == True
    assert is_balance_sufficient(50, 100) == True
    assert is_balance_sufficient(150, 100) == False

def test_process_withdrawal_success():
    assert process_withdrawal(50, 100) == 50
    assert process_withdrawal(100, 100) == 0

def test_process_withdrawal_invalid():
    assert process_withdrawal(55, 100) == "Invalid Amount"
    assert process_withdrawal(0, 100) == "Invalid Amount"

def test_process_withdrawal_insufficient():
    assert process_withdrawal(150, 100) == "Insufficient Funds"
