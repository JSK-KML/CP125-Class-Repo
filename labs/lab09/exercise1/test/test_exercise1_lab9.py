import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise1.py')
_spec = importlib.util.spec_from_file_location("exercise1_lab9", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
explore_data = _module.explore_data

_lab_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_data_file = os.path.join(_lab_dir, "data", "students.csv")


def test_total_students():
    result = explore_data(_data_file)
    assert result["total_students"] == 25


def test_subjects_list():
    result = explore_data(_data_file)
    assert result["subjects"] == ["Math", "Science", "English"]


def test_math_average():
    result = explore_data(_data_file)
    assert result["math_average"] == pytest.approx(84.0, abs=0.1)


def test_highest_math_student():
    result = explore_data(_data_file)
    assert result["highest_math_student"] == "Hassan"


def test_return_type():
    result = explore_data(_data_file)
    assert isinstance(result, dict)


def test_all_keys_present():
    result = explore_data(_data_file)
    expected_keys = {"total_students", "subjects", "math_average", "highest_math_student"}
    assert set(result.keys()) == expected_keys


def test_subjects_order():
    result = explore_data(_data_file)
    assert result["subjects"][0] == "Math"
    assert result["subjects"][1] == "Science"
    assert result["subjects"][2] == "English"


def test_total_students_positive():
    result = explore_data(_data_file)
    assert result["total_students"] > 0


def test_math_average_range():
    result = explore_data(_data_file)
    assert 0 <= result["math_average"] <= 100


def test_highest_math_student_type():
    result = explore_data(_data_file)
    assert isinstance(result["highest_math_student"], str)
