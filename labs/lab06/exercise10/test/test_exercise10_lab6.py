import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise10.py')
_spec = importlib.util.spec_from_file_location("exercise10_lab6", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
get_unique_attendees = _module.get_unique_attendees
count_unique_events = _module.count_unique_events
filter_by_threshold = _module.filter_by_threshold
find_frequent_attendees = _module.find_frequent_attendees

# Tests for get_unique_attendees
def test_get_unique_attendees_standard():
    logs = [("A1", "E1"), ("A2", "E2"), ("A1", "E3")]
    assert get_unique_attendees(logs) == {"A1", "A2"}

def test_get_unique_attendees_single():
    logs = [("A1", "E1"), ("A1", "E2")]
    assert get_unique_attendees(logs) == {"A1"}

def test_get_unique_attendees_all_different():
    logs = [("A1", "E1"), ("A2", "E2"), ("A3", "E3")]
    assert get_unique_attendees(logs) == {"A1", "A2", "A3"}

def test_get_unique_attendees_empty():
    logs = []
    assert get_unique_attendees(logs) == set()

# Tests for count_unique_events
def test_count_unique_events_multiple():
    logs = [("A1", "E1"), ("A1", "E2"), ("A2", "E3")]
    assert count_unique_events(logs, "A1") == 2

def test_count_unique_events_with_duplicates():
    logs = [("A1", "E1"), ("A1", "E1"), ("A1", "E2")]
    assert count_unique_events(logs, "A1") == 2

def test_count_unique_events_single():
    logs = [("A1", "E1"), ("A2", "E2")]
    assert count_unique_events(logs, "A1") == 1

def test_count_unique_events_none():
    logs = [("A2", "E1"), ("A3", "E2")]
    assert count_unique_events(logs, "A1") == 0

# Tests for filter_by_threshold
def test_filter_by_threshold_multiple_qualify():
    attendees = {"A1", "A2", "A3"}
    logs = [("A1", "E1"), ("A1", "E2"), ("A2", "E1"), ("A2", "E2"), ("A3", "E1")]
    assert filter_by_threshold(attendees, logs, 2) == ["A1", "A2"]

def test_filter_by_threshold_none_qualify():
    attendees = {"A1", "A2"}
    logs = [("A1", "E1"), ("A2", "E1")]
    assert filter_by_threshold(attendees, logs, 3) == []

def test_filter_by_threshold_all_qualify():
    attendees = {"A1", "A2"}
    logs = [("A1", "E1"), ("A1", "E2"), ("A2", "E3"), ("A2", "E4")]
    assert filter_by_threshold(attendees, logs, 1) == ["A1", "A2"]

def test_filter_by_threshold_sorting():
    attendees = {"Z9", "A1", "M5"}
    logs = [("Z9", "E1"), ("Z9", "E2"), ("A1", "E3"), ("A1", "E4"), ("M5", "E5"), ("M5", "E6")]
    assert filter_by_threshold(attendees, logs, 2) == ["A1", "M5", "Z9"]

# Tests for find_frequent_attendees (integration)
def test_find_frequent_attendees_standard():
    logs = [("A1", "E1"), ("A1", "E2"), ("A2", "E1"), ("A1", "E1"), ("A3", "E1"), ("A2", "E2"), ("A2", "E3")]
    assert find_frequent_attendees(logs, 2) == ["A1", "A2"]

def test_find_frequent_attendees_threshold_high():
    logs = [("A1", "E1"), ("A2", "E2"), ("A3", "E3")]
    assert find_frequent_attendees(logs, 2) == []

def test_find_frequent_attendees_all_qualify():
    logs = [("A1", "E1"), ("A1", "E2"), ("A2", "E3"), ("A2", "E4")]
    assert find_frequent_attendees(logs, 1) == ["A1", "A2"]

def test_find_frequent_attendees_empty():
    logs = []
    assert find_frequent_attendees(logs, 1) == []
