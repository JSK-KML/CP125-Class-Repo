
import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise14 import is_safe_time, needs_moisture, should_trigger_pump

def test_is_safe_time_normal():
    assert is_safe_time(8, 25) == True
    assert is_safe_time(10, 25) == False
    assert is_safe_time(12, 25) == False
    assert is_safe_time(16, 25) == False
    assert is_safe_time(17, 25) == True

def test_is_safe_time_hot():
    assert is_safe_time(12, 45) == True # Override!

def test_needs_moisture():
    assert needs_moisture(29) == True
    assert needs_moisture(30) == False
    assert needs_moisture(50) == False

def test_should_trigger_pump():
    # Needs + Safe
    assert should_trigger_pump(20, 8, 25) == True
    # Needs + Not Safe
    assert should_trigger_pump(20, 12, 25) == False
    # Needs + Hot Override
    assert should_trigger_pump(20, 12, 45) == True
    # Doesn't need
    assert should_trigger_pump(40, 8, 25) == False
