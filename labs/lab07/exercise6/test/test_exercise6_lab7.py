import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise6.py')
_spec = importlib.util.spec_from_file_location("exercise6_lab7", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
merge_results = _module.merge_results
get_passing_students = _module.get_passing_students


def test_merge_higher_score_kept():
    existing = {"Ali": 85}
    result = merge_results(existing, {"Ali": 90})
    assert result["Ali"] == 90

def test_merge_lower_score_not_applied():
    existing = {"Ali": 90}
    result = merge_results(existing, {"Ali": 70})
    assert result["Ali"] == 90

def test_merge_new_student_added():
    existing = {"Ali": 85}
    result = merge_results(existing, {"Sara": 70})
    assert result["Sara"] == 70

def test_merge_unaffected_student_preserved():
    existing = {"Ali": 85, "Sara": 70}
    merge_results(existing, {"Ali": 90})
    assert existing["Sara"] == 70

def test_merge_full_example():
    existing = {"Ali": 85, "Sara": 70}
    result = merge_results(existing, {"Ali": 90, "Ahmad": 60})
    assert result == {"Ali": 90, "Sara": 70, "Ahmad": 60}

def test_passing_returns_names_not_scores():
    scores = {"Ali": 90, "Sara": 70}
    result = get_passing_students(scores, 75)
    assert all(isinstance(x, str) for x in result)

def test_passing_correct_names():
    scores = {"Ali": 90, "Sara": 70, "Ahmad": 60}
    assert get_passing_students(scores, 75) == ["Ali"]

def test_passing_sorted():
    scores = {"Zara": 90, "Ali": 85, "Sara": 80}
    assert get_passing_students(scores, 75) == ["Ali", "Sara", "Zara"]

def test_passing_none_qualify():
    scores = {"Ali": 50, "Sara": 40}
    assert get_passing_students(scores, 75) == []

def test_passing_all_qualify():
    scores = {"Ali": 90, "Sara": 85}
    assert get_passing_students(scores, 75) == ["Ali", "Sara"]
