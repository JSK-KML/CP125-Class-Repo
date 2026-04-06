import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise6.py')
_spec = importlib.util.spec_from_file_location("exercise6_lab9", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
critical_inventory = _module.critical_inventory

_lab_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_data_file = os.path.join(_lab_dir, "data", "inventory.csv")


def test_total_products():
    result = critical_inventory(_data_file)
    assert result["total_products"] == 50


def test_critical_count():
    result = critical_inventory(_data_file)
    assert result["critical_count"] == 17


def test_critical_products_type():
    result = critical_inventory(_data_file)
    assert isinstance(result["critical_products"], set)


def test_return_type():
    result = critical_inventory(_data_file)
    assert isinstance(result, dict)


def test_all_keys_present():
    result = critical_inventory(_data_file)
    expected_keys = {"total_products", "critical_count", "critical_products"}
    assert set(result.keys()) == expected_keys


def test_critical_count_matches_set_length():
    result = critical_inventory(_data_file)
    assert result["critical_count"] == len(result["critical_products"])


def test_critical_products_contains_laptop():
    result = critical_inventory(_data_file)
    assert "Laptop_X1" in result["critical_products"]


def test_critical_count_less_than_total():
    result = critical_inventory(_data_file)
    assert result["critical_count"] < result["total_products"]


def test_total_products_positive():
    result = critical_inventory(_data_file)
    assert result["total_products"] > 0


def test_critical_products_non_empty():
    result = critical_inventory(_data_file)
    assert len(result["critical_products"]) > 0
