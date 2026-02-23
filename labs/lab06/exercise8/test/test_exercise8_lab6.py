import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise8.py')
_spec = importlib.util.spec_from_file_location("exercise8_lab6", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
analyze_scores = _module.analyze_scores

def test_standard_case():
    scores = [("S1", 85), ("S2", 90), ("S3", 75), ("S4", 95), ("S5", 80)]
    assert analyze_scores(scores) == (95, 85.0, 2)

def test_all_same_scores():
    scores = [("S1", 80), ("S2", 80), ("S3", 80)]
    assert analyze_scores(scores) == (80, 80.0, 0)

def test_single_student():
    scores = [("S1", 95)]
    assert analyze_scores(scores) == (95, 95.0, 0)

def test_two_students():
    scores = [("S1", 70), ("S2", 90)]
    assert analyze_scores(scores) == (90, 80.0, 1)

def test_all_below_average():
    # If average is higher than all but one score
    scores = [("S1", 50), ("S2", 60), ("S3", 100)]
    assert analyze_scores(scores) == (100, 70.0, 1)

def test_all_above_average():
    # One very low score pulls average down
    scores = [("S1", 100), ("S2", 100), ("S3", 100), ("S4", 10)]
    assert analyze_scores(scores) == (100, 77.5, 3)

def test_decimal_scores():
    scores = [("S1", 85.5), ("S2", 90.5), ("S3", 75.5)]
    # Average: 83.833..., Above: 85.5 and 90.5 = 2 students
    assert analyze_scores(scores) == (90.5, 83.83333333333333, 2)

def test_large_dataset():
    scores = [(f"S{i}", 80 + i) for i in range(10)]
    # Scores: 80, 81, 82, 83, 84, 85, 86, 87, 88, 89
    # Average: 84.5
    # Above avg: 85, 86, 87, 88, 89 = 5 students
    assert analyze_scores(scores) == (89, 84.5, 5)

def test_exact_average():
    scores = [("S1", 100), ("S2", 80), ("S3", 90)]
    # Average: 90.0
    # Above average (>90): only 100 = 1 student
    assert analyze_scores(scores) == (100, 90.0, 1)

def test_many_students_same_high_score():
    scores = [("S1", 95), ("S2", 95), ("S3", 95), ("S4", 70), ("S5", 70)]
    # Average: 85.0
    # Above average: 95, 95, 95 = 3 students
    assert analyze_scores(scores) == (95, 85.0, 3)
