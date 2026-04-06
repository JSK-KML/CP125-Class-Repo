import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise4.py')
_spec = importlib.util.spec_from_file_location("exercise4_lab9", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
show_science_distribution = _module.show_science_distribution
import matplotlib
matplotlib.use('Agg')

_lab_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_data_file = os.path.join(_lab_dir, "data", "students.csv")


def test_returns_student_count():
    result = show_science_distribution(_data_file)
    assert result == 25


def test_return_type():
    result = show_science_distribution(_data_file)
    assert isinstance(result, int)


def test_count_positive():
    result = show_science_distribution(_data_file)
    assert result > 0


def test_count_matches_data():
    result = show_science_distribution(_data_file)
    assert result == 25


def test_function_exists():
    assert callable(show_science_distribution)


def test_accepts_string_parameter():
    result = show_science_distribution(_data_file)
    assert result is not None


def test_returns_integer():
    result = show_science_distribution(_data_file)
    assert type(result) == int


def test_count_not_zero():
    result = show_science_distribution(_data_file)
    assert result != 0


def test_count_reasonable_range():
    result = show_science_distribution(_data_file)
    assert 1 <= result <= 100


def test_multiple_calls_consistent():
    result1 = show_science_distribution(_data_file)
    result2 = show_science_distribution(_data_file)
    assert result1 == result2
