import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise2 import calculate_event_cost

def test_exact_tent_capacity():
    # 12 people, cap 4 -> 3 tents. Price 100/tent. 300. Food 12*10=120. Total 420.
    assert calculate_event_cost(12, 4, 100, 10) == 420.0

def test_tent_remainder():
    # 13 people, cap 4 -> 4 tents. Price 100 -> 400. Food 13*10=130. Total 530.
    assert calculate_event_cost(13, 4, 100, 10) == 530.0

def test_one_person():
    # 1 person, cap 4 -> 1 tent (100). Food 10. Total 110.
    assert calculate_event_cost(1, 4, 100, 10) == 110.0

def test_zero_participants():
    # 0 people -> 0 tents, 0 food. Total 0.
    assert calculate_event_cost(0, 4, 100, 10) == 0.0

def test_large_capacity():
    # 10 people, cap 20 -> 1 tent (100). Food 10*10=100. Total 200.
    assert calculate_event_cost(10, 20, 100, 10) == 200.0

def test_capacity_one():
    # 5 people, cap 1 -> 5 tents (500). Food 5*10=50. Total 550.
    assert calculate_event_cost(5, 1, 100, 10) == 550.0

def test_expensive_tents():
    # 10 people, cap 10 -> 1 tent (1000). Food 10*10=100. Total 1100.
    assert calculate_event_cost(10, 10, 1000, 10) == 1100.0

def test_expensive_food():
    # 10 people, cap 10 -> 1 tent (100). Food 10*50=500. Total 600.
    assert calculate_event_cost(10, 10, 100, 50) == 600.0

def test_free_everything():
    # 100 people. 0 cost.
    assert calculate_event_cost(100, 10, 0, 0) == 0.0

def test_complex_numbers():
    # 47 people (Lab Example). Cap 6. -> 8 tents.
    # 8 * 100 = 800.
    # 47 * 25 = 1175.
    # Total = 1975.
    assert calculate_event_cost(47, 6, 100, 25) == 1975.0
