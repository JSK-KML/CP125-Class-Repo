
import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise13 import get_rate_per_kg, get_express_charge, calculate_shipping_quote

def test_get_rate_per_kg():
    assert get_rate_per_kg("Domestic") == 5.0
    assert get_rate_per_kg("International") == 15.0

def test_get_express_charge():
    assert get_express_charge(True) == 10.0
    assert get_express_charge(False) == 0.0

def test_calculate_shipping_quote_domestic():
    # 2kg * 5.0 + 0 = 10.0
    assert calculate_shipping_quote(2, "Domestic", False) == 10.0
    # 2kg * 5.0 + 10.0 = 20.0
    assert calculate_shipping_quote(2, "Domestic", True) == 20.0

def test_calculate_shipping_quote_intl():
    # 2kg * 15.0 + 0 = 30.0
    assert calculate_shipping_quote(2, "International", False) == 30.0
    # 2kg * 15.0 + 10.0 = 40.0
    assert calculate_shipping_quote(2, "International", True) == 40.0
