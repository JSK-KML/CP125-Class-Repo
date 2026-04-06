import pytest
import importlib.util
import os
import pandas as pd

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise8.py')
_spec = importlib.util.spec_from_file_location("exercise8_lab9", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
plot_subject_maximums = _module.plot_subject_maximums

_lab_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_data_file = os.path.join(_lab_dir, "data", "students.csv")


def test_return_value():
    result = plot_subject_maximums(_data_file)
    assert result == 25


def test_return_type():
    result = plot_subject_maximums(_data_file)
    assert isinstance(result, int)


def test_return_positive():
    result = plot_subject_maximums(_data_file)
    assert result > 0


def test_data_file_loaded():
    df = pd.read_csv(_data_file)
    assert len(df) == 25


def test_data_has_physics():
    df = pd.read_csv(_data_file)
    assert 'Physics' in df.columns


def test_data_has_chemistry():
    df = pd.read_csv(_data_file)
    assert 'Chemistry' in df.columns


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
    assert callable(plot_subject_maximums)
