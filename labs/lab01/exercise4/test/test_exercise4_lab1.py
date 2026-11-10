import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise4 import get_hourly_rate

def test_electric_day():
    assert get_hourly_rate("Electric", 12) == 2.00

def test_electric_night():
    assert get_hourly_rate("Electric", 23) == 2.00

def test_electric_midnight():
    assert get_hourly_rate("Electric", 0) == 2.00

def test_hybrid_day_fail():
    # Hybrid pays full price during day (e.g. 1pm / 13:00)
    assert get_hourly_rate("Hybrid", 13) == 5.00

def test_hybrid_night_before_midnight():
    # Hybrid pays cheap rate after 10pm (22)
    assert get_hourly_rate("Hybrid", 22) == 2.00

def test_hybrid_night_after_midnight():
    # Hybrid pays cheap rate before 6am
    assert get_hourly_rate("Hybrid", 5) == 2.00

def test_hybrid_boundary_morning():
    # Exactly 6am should still be cheap (or cheap ends at 6? Problem says "between 22 and 6")
    # Usually "between 10pm and 6am" implies inclusive of the range hours, or up to.
    # Let's assume inclusive for safety or stick to safer inner bounds.
    # Problem says: "between 10pm (22) and 6am (6)"
    # Let's assume inclusive [0, 6] and [22, 23].
    assert get_hourly_rate("Hybrid", 6) == 2.00

def test_hybrid_boundary_morning_fail():
    # 7am is definitely not night
    assert get_hourly_rate("Hybrid", 7) == 5.00

def test_other_car_day():
    assert get_hourly_rate("Sedan", 12) == 5.00

def test_other_car_night():
    assert get_hourly_rate("SUV", 23) == 5.00
