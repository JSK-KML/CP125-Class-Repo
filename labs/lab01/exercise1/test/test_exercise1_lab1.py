import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise1 import is_budget_sufficient

def test_budget_exact_match():
    # 100km one way = 200km round trip. 10km/l -> 20 liters. RM2.00/l -> RM40.00. Budget 40. True
    assert is_budget_sufficient(100, 10, 2.00, 40) == True

def test_budget_insufficient():
    # 100km one way = 200km total. 10km/l -> 20L. RM2.00/l -> RM40. Budget 39. False
    assert is_budget_sufficient(100, 10, 2.00, 39) == False

def test_zero_distance():
    # 0km -> 0 cost. Budget 0. True
    assert is_budget_sufficient(0, 10, 2.05, 0) == True

def test_high_efficiency_car():
    # 500km one way = 1000km. 50km/l -> 20L. RM2.00/l -> RM40. Budget 50. True
    assert is_budget_sufficient(500, 50, 2.00, 50) == True

def test_low_efficiency_car():
    # 100km one way = 200km. 5km/l -> 40L. RM2.00/l -> RM80. Budget 50. False
    assert is_budget_sufficient(100, 5, 2.00, 50) == False

def test_expensive_fuel():
    # 10km one way = 20km. 10km/l -> 2L. RM100/l -> RM200. Budget 150. False
    assert is_budget_sufficient(10, 10, 100.00, 150) == False

def test_cheap_fuel():
    # 10km one way = 20km. 10km/l -> 2L. RM0.50/l -> RM1.00. Budget 2. True
    assert is_budget_sufficient(10, 10, 0.50, 2) == True

def test_large_budget():
    # Cost RM40, Budget RM1000. True
    assert is_budget_sufficient(100, 10, 2.00, 1000) == True

def test_float_precision_edge():
    # 1.5km one way = 3.0km. 3km/l -> 1L. RM2.00/l -> RM2.00. Budget 1.99. False
    assert is_budget_sufficient(1.5, 3, 2.00, 1.99) == False

def test_rounding_success():
    # 1.5km one way = 3.0km. 3km/l -> 1L. RM2.00/l -> RM2.00. Budget 2.00. True
    assert is_budget_sufficient(1.5, 3, 2.00, 2.00) == True
