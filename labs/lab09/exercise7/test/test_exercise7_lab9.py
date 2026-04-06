import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise7.py')
_spec = importlib.util.spec_from_file_location("exercise7_lab9", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
promotion_candidates = _module.promotion_candidates

_lab_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_data_file = os.path.join(_lab_dir, "data", "employees.csv")


def test_average_performance():
    result = promotion_candidates(_data_file)
    assert result["average_performance"] == pytest.approx(84.3, abs=0.1)


def test_min_years_required():
    result = promotion_candidates(_data_file)
    assert result["min_years_required"] == 2


def test_candidate_count():
    result = promotion_candidates(_data_file)
    assert result["candidate_count"] == 28


def test_candidate_names_type():
    result = promotion_candidates(_data_file)
    assert isinstance(result["candidate_names"], set)


def test_return_type():
    result = promotion_candidates(_data_file)
    assert isinstance(result, dict)


def test_all_keys_present():
    result = promotion_candidates(_data_file)
    expected_keys = {"average_performance", "min_years_required", "candidate_count", "candidate_names"}
    assert set(result.keys()) == expected_keys


def test_candidate_count_matches_names_length():
    result = promotion_candidates(_data_file)
    assert result["candidate_count"] == len(result["candidate_names"])


def test_candidate_names_contains_sarah():
    result = promotion_candidates(_data_file)
    assert "Sarah Lee" in result["candidate_names"]


def test_average_performance_range():
    result = promotion_candidates(_data_file)
    assert 0 <= result["average_performance"] <= 100


def test_candidate_count_positive():
    result = promotion_candidates(_data_file)
    assert result["candidate_count"] > 0
