import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise6.py')
_spec = importlib.util.spec_from_file_location("exercise6_lab6", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
manage_roster = _module.manage_roster

def test_no_drops_full_class():
    """Test when class is full and no drops"""
    enrolled = {"Alice", "Bob", "Charlie", "Diana", "Eva", "Frank", "George"}
    drop_requests = []
    waitlist = {"Henry", "Iris"}
    result = manage_roster(enrolled, drop_requests, waitlist)
    assert result == 7

def test_few_drops_still_above_minimum():
    """Test when some students drop but class stays above 5"""
    enrolled = {"Alice", "Bob", "Charlie", "Diana", "Eva", "Frank", "George"}
    drop_requests = ["Alice", "Bob"]
    waitlist = {"Henry", "Iris"}
    result = manage_roster(enrolled, drop_requests, waitlist)
    assert result == 5  # 7 - 2 = 5, no need to add from waitlist

def test_drops_below_minimum_add_from_waitlist():
    """Test the example from lab description"""
    enrolled = {"Alice", "Bob", "Charlie", "Diana", "Eva", "Frank", "George"}
    drop_requests = ["Alice", "Charlie", "Diana", "Eva"]
    waitlist = {"Henry", "Iris", "Jack"}
    result = manage_roster(enrolled, drop_requests, waitlist)
    assert result == 6  # 3 remaining + 3 from waitlist = 6

def test_drops_below_minimum_waitlist_reaches_7():
    """Test when waitlist is large enough to reach 7"""
    enrolled = {"Alice", "Bob", "Charlie", "Diana", "Eva", "Frank", "George"}
    drop_requests = ["Alice", "Charlie", "Diana", "Eva"]
    waitlist = {"Henry", "Iris", "Jack", "Kate", "Leo"}
    result = manage_roster(enrolled, drop_requests, waitlist)
    assert result == 7  # Should fill to exactly 7

def test_all_drop_empty_waitlist():
    """Test when all students drop and no waitlist"""
    enrolled = {"Alice", "Bob", "Charlie"}
    drop_requests = ["Alice", "Bob", "Charlie"]
    waitlist = set()
    result = manage_roster(enrolled, drop_requests, waitlist)
    assert result == 0

def test_all_drop_with_waitlist():
    """Test when all students drop but waitlist available"""
    enrolled = {"Alice", "Bob", "Charlie"}
    drop_requests = ["Alice", "Bob", "Charlie"]
    waitlist = {"Henry", "Iris", "Jack", "Kate", "Leo", "Mary", "Nick"}
    result = manage_roster(enrolled, drop_requests, waitlist)
    assert result == 7  # Should fill to 7 from waitlist

def test_drop_nonexistent_student():
    """Test dropping a student who isn't enrolled (should be ignored)"""
    enrolled = {"Alice", "Bob", "Charlie", "Diana", "Eva"}
    drop_requests = ["Zorro", "Alice"]
    waitlist = {"Henry"}
    result = manage_roster(enrolled, drop_requests, waitlist)
    assert result == 5  # 5 - 1 (Alice) = 4, then adds 1 from waitlist to reach 5


def test_empty_enrolled_empty_waitlist():
    """Test edge case: no students at all"""
    enrolled = set()
    drop_requests = []
    waitlist = set()
    result = manage_roster(enrolled, drop_requests, waitlist)
    assert result == 0

def test_empty_enrolled_with_waitlist():
    """Test starting with no enrolled but having waitlist"""
    enrolled = set()
    drop_requests = []
    waitlist = {"A", "B", "C", "D", "E", "F", "G", "H"}
    result = manage_roster(enrolled, drop_requests, waitlist)
    assert result == 7  # Should add 7 from waitlist

def test_exactly_5_students_no_action():
    """Test when exactly at minimum (5), no action needed"""
    enrolled = {"Alice", "Bob", "Charlie", "Diana", "Eva"}
    drop_requests = []
    waitlist = {"Henry", "Iris"}
    result = manage_roster(enrolled, drop_requests, waitlist)
    assert result == 5  # No drops, stays at 5

def test_drops_to_exactly_5():
    """Test when drops result in exactly 5 students"""
    enrolled = {"Alice", "Bob", "Charlie", "Diana", "Eva", "Frank", "George"}
    drop_requests = ["Alice", "Bob"]
    waitlist = {"Henry"}
    result = manage_roster(enrolled, drop_requests, waitlist)
    assert result == 5  # 7 - 2 = 5, at minimum, no need to add

def test_drops_to_4_small_waitlist():
    """Test when drops to 4 and waitlist has only 1 student"""
    enrolled = {"Alice", "Bob", "Charlie", "Diana", "Eva", "Frank"}
    drop_requests = ["Alice", "Bob"]
    waitlist = {"Henry"}
    result = manage_roster(enrolled, drop_requests, waitlist)
    assert result == 5  # 6 - 2 = 4, add 1 from waitlist = 5
