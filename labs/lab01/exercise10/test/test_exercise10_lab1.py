
import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise10 import calculate_base_usage, apply_mode_bonus, has_enough_battery

def test_calculate_base_usage():
    assert calculate_base_usage(10) == 1.5
    assert calculate_base_usage(20) == 3.0
    assert calculate_base_usage(100) == 15.0

def test_apply_mode_bonus():
    assert apply_mode_bonus(10, False) == 10
    assert apply_mode_bonus(10, True) == 15
    assert apply_mode_bonus(20, True) == 30

def test_has_enough_battery_normal():
    # 100m round trip = 200m. Usage = (200/10)*1.5 = 30%.
    assert has_enough_battery(100, 31, False) == True
    assert has_enough_battery(100, 30, False) == True
    assert has_enough_battery(100, 29, False) == False

def test_has_enough_battery_sport():
    # 100m round trip = 200m. Base = 30%. Sport = 30*1.5 = 45%.
    assert has_enough_battery(100, 46, True) == True
    assert has_enough_battery(100, 45, True) == True
    assert has_enough_battery(100, 44, True) == False
