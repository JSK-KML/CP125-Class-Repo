import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise8 import calculate_bounce_height, is_ball_stopped, calculate_bounce_count, calculate_total_distance

# Tests for calculate_bounce_height
def test_bounce_height_from_100():
    # 100 * 0.8 = 80
    assert calculate_bounce_height(100) == 80

def test_bounce_height_from_80():
    # 80 * 0.8 = 64
    assert calculate_bounce_height(80) == 64

def test_bounce_height_from_10():
    # 10 * 0.8 = 8
    assert calculate_bounce_height(10) == 8

def test_bounce_height_small():
    # 1.25 * 0.8 = 1.0
    assert calculate_bounce_height(1.25) == 1.0

# Tests for is_ball_stopped
def test_ball_stopped_at_zero():
    assert is_ball_stopped(0) == True

def test_ball_stopped_below_one():
    assert is_ball_stopped(0.5) == True

def test_ball_not_stopped_at_one():
    assert is_ball_stopped(1) == False

def test_ball_not_stopped_above_one():
    assert is_ball_stopped(5) == False

# Tests for calculate_bounce_count
def test_bounce_count_from_100():
    # Start at 100, bounces: 80, 64, 51.2, 40.96, 32.77, 26.21, 20.97, 16.78, 13.42, 10.74, 8.59, 6.87, 5.50, 4.40, 3.52, 2.81, 2.25, 1.80, 1.44, 1.15, 0.92
    # Total bounces = 21 (until height < 1)
    assert calculate_bounce_count(100) == 21

def test_bounce_count_from_50():
    assert calculate_bounce_count(50) == 18

def test_bounce_count_from_10():
    # 10 -> 8 -> 6.4 -> 5.12 -> 4.1 -> 3.28 -> 2.62 -> 2.1 -> 1.68 -> 1.34 -> 1.07 -> 0.86
    assert calculate_bounce_count(10) == 11

def test_bounce_count_from_1():
    # Start at 1, first bounce is 0.8 which is < 1, so 1 bounce occurs
    assert calculate_bounce_count(1) == 1

def test_bounce_count_from_0():
    # Start at 0, no bounces
    assert calculate_bounce_count(0) == 0

# Tests for calculate_total_distance
def test_total_distance_from_100():
    # Verify total distance is calculated correctly
    distance = calculate_total_distance(100)
    # Distance should be around 900 (100 + 80*2 + 64*2 + ...)
    assert distance > 800
    assert distance < 1000

def test_total_distance_from_50():
    distance = calculate_total_distance(50)
    assert distance > 400
    assert distance < 500

def test_total_distance_from_10():
    distance = calculate_total_distance(10)
    assert distance > 80
    assert distance < 100

def test_total_distance_from_1():
    # Start at 1, drops 1, bounces to 0.8 (< 1, stops)
    # Total distance = 1 (initial drop) + 0.8 (up) = 1.8
    distance = calculate_total_distance(1)
    assert distance > 1.5
    assert distance < 2.0

def test_total_distance_from_0():
    assert calculate_total_distance(0) == 0
