import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise2.py')
_spec = importlib.util.spec_from_file_location("exercise2_lab9", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
compare_averages = _module.compare_averages

_lab_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_data_file = os.path.join(_lab_dir, "data", "students.csv")


def test_math_average():
    result = compare_averages(_data_file)
    assert result["Math"] == pytest.approx(84.0, abs=0.1)


def test_science_average():
    result = compare_averages(_data_file)
    assert result["Science"] == pytest.approx(82.9, abs=0.1)


def test_english_average():
    result = compare_averages(_data_file)
    assert result["English"] == pytest.approx(84.4, abs=0.1)


def test_best_subject():
    result = compare_averages(_data_file)
    assert result["best_subject"] == "English"


def test_worst_subject():
    result = compare_averages(_data_file)
    assert result["worst_subject"] == "Science"


def test_return_type():
    result = compare_averages(_data_file)
    assert isinstance(result, dict)


def test_all_keys_present():
    result = compare_averages(_data_file)
    expected_keys = {"Math", "Science", "English", "best_subject", "worst_subject"}
    assert set(result.keys()) == expected_keys


def test_all_averages_positive():
    result = compare_averages(_data_file)
    assert result["Math"] > 0
    assert result["Science"] > 0
    assert result["English"] > 0


def test_subject_name_types():
    result = compare_averages(_data_file)
    assert isinstance(result["best_subject"], str)
    assert isinstance(result["worst_subject"], str)


def test_best_worst_different():
    result = compare_averages(_data_file)
    assert result["best_subject"] != result["worst_subject"]
