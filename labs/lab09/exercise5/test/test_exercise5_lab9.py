import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise5.py')
_spec = importlib.util.spec_from_file_location("exercise5_lab9", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
high_performers = _module.high_performers

_lab_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_data_file = os.path.join(_lab_dir, "data", "students.csv")


def test_count():
    result = high_performers(_data_file)
    assert result["count"] == 9


def test_names_type():
    result = high_performers(_data_file)
    assert isinstance(result["names"], set)


def test_return_type():
    result = high_performers(_data_file)
    assert isinstance(result, dict)


def test_all_keys_present():
    result = high_performers(_data_file)
    expected_keys = {"count", "names"}
    assert set(result.keys()) == expected_keys


def test_count_positive():
    result = high_performers(_data_file)
    assert result["count"] > 0


def test_count_matches_names_length():
    result = high_performers(_data_file)
    assert result["count"] == len(result["names"])


def test_names_contains_nadia():
    result = high_performers(_data_file)
    assert "Nadia" in result["names"]


def test_names_contains_hana():
    result = high_performers(_data_file)
    assert "Hana" in result["names"]


def test_count_less_than_total():
    result = high_performers(_data_file)
    assert result["count"] < 25


def test_names_non_empty():
    result = high_performers(_data_file)
    assert len(result["names"]) > 0
