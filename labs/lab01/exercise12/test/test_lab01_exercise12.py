
import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise12 import is_critical_hit, calculate_raw_damage, calculate_final_health

def test_is_critical_hit():
    assert is_critical_hit(71) == True
    assert is_critical_hit(70) == False
    assert is_critical_hit(50) == False

def test_calculate_raw_damage():
    assert calculate_raw_damage(10, False) == 10
    assert calculate_raw_damage(10, True) == 20

def test_calculate_final_health_positive():
    # 100 - (50 - 20) = 70
    assert calculate_final_health(100, 50, 20) == 70

def test_calculate_final_health_no_damage():
    # 100 - (10 - 20) -> 100 - 0 = 100
    assert calculate_final_health(100, 10, 20) == 100

def test_calculate_final_health_zero():
    # 10 - (50 - 20) = 10 - 30 -> 0
    assert calculate_final_health(10, 50, 20) == 0

def test_combined_crit_hit():
    health = 100
    base = 50
    luck = 80 # Crit!
    defense = 10
    
    crit = is_critical_hit(luck) # True
    raw = calculate_raw_damage(base, crit) # 100
    final = calculate_final_health(health, raw, defense) # 100 - (100-10) = 10
    assert final == 10
