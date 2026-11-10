import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise7 import check_collision

def test_no_collision_far_apart():
    # Rectangles far apart
    assert check_collision(0, 0, 10, 10, 50, 50, 10, 10) == False

def test_collision_overlap():
    # Rectangles overlapping
    assert check_collision(0, 0, 20, 20, 10, 10, 20, 20) == True

def test_collision_same_position():
    # Rectangles at same position
    assert check_collision(0, 0, 10, 10, 0, 0, 10, 10) == True

def test_no_collision_touching_edges():
    # Rectangles touching but not overlapping
    assert check_collision(0, 0, 10, 10, 10, 0, 10, 10) == False

def test_collision_one_inside_other():
    # Small rectangle inside large one
    assert check_collision(0, 0, 100, 100, 25, 25, 10, 10) == True

def test_no_collision_above():
    # Rect 1 above Rect 2
    assert check_collision(0, 0, 10, 10, 0, 20, 10, 10) == False

def test_no_collision_below():
    # Rect 1 below Rect 2
    assert check_collision(0, 20, 10, 10, 0, 0, 10, 10) == False

def test_no_collision_left():
    # Rect 1 to the left of Rect 2
    assert check_collision(0, 0, 10, 10, 20, 0, 10, 10) == False

def test_no_collision_right():
    # Rect 1 to the right of Rect 2
    assert check_collision(20, 0, 10, 10, 0, 0, 10, 10) == False

def test_collision_corner_overlap():
    # Just corners overlapping
    assert check_collision(0, 0, 15, 15, 10, 10, 15, 15) == True
