import pytest
import importlib.util
import os
import pandas as pd

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise9.py')
_spec = importlib.util.spec_from_file_location("exercise9_lab9", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
compare_subject_distributions = _module.compare_subject_distributions

_lab_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_data_file = os.path.join(_lab_dir, "data", "students.csv")


def test_return_value():
    result = compare_subject_distributions(_data_file)
    assert result == 25


def test_return_type():
    result = compare_subject_distributions(_data_file)
    assert isinstance(result, int)


def test_return_positive():
    result = compare_subject_distributions(_data_file)
    assert result > 0


def test_data_file_loaded():
    df = pd.read_csv(_data_file)
    assert len(df) == 25


def test_data_has_math():
    df = pd.read_csv(_data_file)
    assert 'Math' in df.columns


def test_data_has_science():
    df = pd.read_csv(_data_file)
    assert 'Science' in df.columns


def test_data_has_english():
    df = pd.read_csv(_data_file)
    assert 'English' in df.columns


def test_function_exists():
    assert callable(compare_subject_distributions)


def test_data_math_non_empty():
    df = pd.read_csv(_data_file)
    assert len(df['Math']) > 0


def test_data_science_non_empty():
    df = pd.read_csv(_data_file)
    assert len(df['Science']) > 0
