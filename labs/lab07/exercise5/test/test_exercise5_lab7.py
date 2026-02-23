import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise5.py')
_spec = importlib.util.spec_from_file_location("exercise5_lab7", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
find_at_risk_departments = _module.find_at_risk_departments


def test_majority_below_threshold():
    dept = {"CS": {"Ali": 85, "Sara": 55, "Zaki": 62}}
    assert find_at_risk_departments(dept, 65) == ["CS"]

def test_exactly_half_not_at_risk():
    # 1 out of 2 is exactly half — NOT strictly more than half
    dept = {"Math": {"A": 90, "B": 40}}
    assert find_at_risk_departments(dept, 65) == []

def test_none_below_threshold():
    dept = {"Math": {"Hana": 90, "Reza": 88}}
    assert find_at_risk_departments(dept, 65) == []

def test_all_below_threshold():
    dept = {"English": {"Tom": 45, "Jay": 50, "Lin": 48}}
    assert find_at_risk_departments(dept, 65) == ["English"]

def test_single_student_below():
    dept = {"CS": {"Ali": 50}}
    assert find_at_risk_departments(dept, 65) == ["CS"]

def test_single_student_above():
    dept = {"CS": {"Ali": 80}}
    assert find_at_risk_departments(dept, 65) == []

def test_empty_departments():
    assert find_at_risk_departments({}, 65) == []

def test_multiple_at_risk_sorted():
    dept = {
        "Zebra": {"A": 30, "B": 40, "C": 50},
        "Apple": {"X": 30, "Y": 40, "Z": 50},
    }
    assert find_at_risk_departments(dept, 65) == ["Apple", "Zebra"]

def test_no_departments_at_risk():
    dept = {
        "CS": {"Ali": 85, "Sara": 90},
        "Math": {"Hana": 88, "Reza": 92},
    }
    assert find_at_risk_departments(dept, 65) == []

def test_full_example():
    departments = {
        "CS":      {"Ali": 85, "Sara": 55, "Zaki": 62},
        "Math":    {"Hana": 90, "Reza": 88},
        "English": {"Tom": 45, "Jay": 50, "Lin": 48},
    }
    assert find_at_risk_departments(departments, 65) == ["CS", "English"]
