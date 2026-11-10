import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise3 import validate_entry

def test_director_success():
    assert validate_entry("Director", 1122) == True

def test_security_success():
    assert validate_entry("Security", 9900) == True

def test_director_wrong_pin():
    assert validate_entry("Director", 9900) == False

def test_security_wrong_pin():
    assert validate_entry("Security", 1122) == False

def test_wrong_name_correct_pin():
    assert validate_entry("Admin", 1122) == False

def test_lowercase_name_fail():
    assert validate_entry("director", 1122) == False

def test_whitespace_fail():
    assert validate_entry("Director ", 1122) == False

def test_security_uppercase_fail():
    assert validate_entry("SECURITY", 9900) == False

def test_empty_strings():
    assert validate_entry("", 0) == False

def test_random_fail():
    assert validate_entry("Hacker", 1234) == False
