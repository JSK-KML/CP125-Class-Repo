import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise6 import is_leap_year

def test_leap_year_divisible_by_4():
    # 2024 is divisible by 4 and not by 100
    assert is_leap_year(2024) == True

def test_leap_year_divisible_by_400():
    # 2000 is divisible by 400
    assert is_leap_year(2000) == True

def test_not_leap_year_divisible_by_100():
    # 1900 is divisible by 100 but not by 400
    assert is_leap_year(1900) == False

def test_not_leap_year_not_divisible_by_4():
    # 2023 is not divisible by 4
    assert is_leap_year(2023) == False

def test_leap_year_2020():
    # Recent leap year
    assert is_leap_year(2020) == True

def test_not_leap_year_2021():
    # Not a leap year
    assert is_leap_year(2021) == False

def test_leap_year_1600():
    # Divisible by 400
    assert is_leap_year(1600) == True

def test_not_leap_year_1700():
    # Divisible by 100 but not 400
    assert is_leap_year(1700) == False

def test_not_leap_year_1800():
    # Divisible by 100 but not 400
    assert is_leap_year(1800) == False

def test_leap_year_2400():
    # Future leap year divisible by 400
    assert is_leap_year(2400) == True
