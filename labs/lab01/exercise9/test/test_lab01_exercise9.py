import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise9 import calculate_xp_required, can_level_up, calculate_final_level, calculate_remaining_xp

# Tests for calculate_xp_required
def test_xp_required_level_1():
    # Level 1 -> 2 requires 100 XP
    assert calculate_xp_required(1) == 100

def test_xp_required_level_2():
    # Level 2 -> 3 requires 200 XP
    assert calculate_xp_required(2) == 200

def test_xp_required_level_3():
    # Level 3 -> 4 requires 300 XP
    assert calculate_xp_required(3) == 300

def test_xp_required_level_10():
    # Level 10 -> 11 requires 1000 XP
    assert calculate_xp_required(10) == 1000

# Tests for can_level_up
def test_can_level_up_exact():
    assert can_level_up(100, 100) == True

def test_can_level_up_enough():
    assert can_level_up(150, 100) == True

def test_cannot_level_up_insufficient():
    assert can_level_up(99, 100) == False

def test_cannot_level_up_zero():
    assert can_level_up(0, 100) == False

# Tests for calculate_final_level
def test_final_level_from_100_xp():
    # 100 XP -> Level 2, 0 remaining
    assert calculate_final_level(100) == 2

def test_final_level_from_300_xp():
    # 300 XP -> Level 3 (100 + 200), 0 remaining
    assert calculate_final_level(300) == 3

def test_final_level_from_600_xp():
    # 600 XP -> Level 4 (100 + 200 + 300), 0 remaining
    assert calculate_final_level(600) == 4

def test_final_level_with_leftover():
    # 650 XP -> Level 4, 50 remaining
    assert calculate_final_level(650) == 4

def test_final_level_not_enough_for_level_2():
    # 50 XP -> Level 1, 50 remaining
    assert calculate_final_level(50) == 1

def test_final_level_zero_xp():
    # 0 XP -> Level 1, 0 remaining
    assert calculate_final_level(0) == 1

def test_final_level_large_xp():
    # 5500 XP -> 100+200+300+400+500+600+700+800+900+1000 = 5500 -> Level 11, 0 remaining
    assert calculate_final_level(5500) == 11

def test_final_level_large_xp_with_remainder():
    # 5600 XP -> Level 11, 100 remaining
    assert calculate_final_level(5600) == 11

# Tests for calculate_remaining_xp
def test_remaining_xp_from_100():
    # 100 XP -> Level 2, 0 remaining
    assert calculate_remaining_xp(100) == 0

def test_remaining_xp_from_300():
    # 300 XP -> Level 3, 0 remaining
    assert calculate_remaining_xp(300) == 0

def test_remaining_xp_from_600():
    # 600 XP -> Level 4, 0 remaining
    assert calculate_remaining_xp(600) == 0

def test_remaining_xp_with_leftover():
    # 650 XP -> Level 4, 50 remaining
    assert calculate_remaining_xp(650) == 50

def test_remaining_xp_not_enough_for_level_2():
    # 50 XP -> Level 1, 50 remaining
    assert calculate_remaining_xp(50) == 50

def test_remaining_xp_zero():
    # 0 XP -> Level 1, 0 remaining
    assert calculate_remaining_xp(0) == 0

def test_remaining_xp_large():
    # 5500 XP -> Level 11, 0 remaining
    assert calculate_remaining_xp(5500) == 0

def test_remaining_xp_large_with_remainder():
    # 5600 XP -> Level 11, 100 remaining
    assert calculate_remaining_xp(5600) == 100
