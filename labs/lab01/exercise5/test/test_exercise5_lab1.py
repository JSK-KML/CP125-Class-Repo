import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise5 import is_valid_triangle

def test_equilateral():
    assert is_valid_triangle(10, 10, 10) == True

def test_isosceles():
    assert is_valid_triangle(5, 5, 8) == True

def test_scalene():
    assert is_valid_triangle(3, 4, 5) == True

def test_invalid_flat():
    # Sum of 1+2 = 3. Not a triangle.
    assert is_valid_triangle(1, 2, 3) == False

def test_invalid_impossible():
    # Sum 1+2=3 which is less than 4.
    assert is_valid_triangle(1, 2, 4) == False

def test_zero_sides():
    assert is_valid_triangle(0, 0, 0) == False
    assert is_valid_triangle(5, 0, 5) == False

def test_negative_sides():
    assert is_valid_triangle(-1, 5, 5) == False

def test_float_sides():
    assert is_valid_triangle(3.5, 4.5, 5.5) == True

def test_large_numbers():
    assert is_valid_triangle(1000, 1000, 1500) == True
