import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise1.py')
_spec = importlib.util.spec_from_file_location("exercise1_lab7", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
process_actions = _module.process_actions


def test_borrow_reduces_count():
    catalog = {"978-A": 3}
    process_actions(catalog, [("BORROW", "978-A")])
    assert catalog["978-A"] == 2

def test_borrow_when_zero_copies_skipped():
    catalog = {"978-B": 0}
    process_actions(catalog, [("BORROW", "978-B")])
    assert catalog["978-B"] == 0

def test_return_increases_count():
    catalog = {"978-A": 1}
    process_actions(catalog, [("RETURN", "978-A")])
    assert catalog["978-A"] == 2

def test_unknown_isbn_skipped():
    catalog = {"978-A": 2}
    process_actions(catalog, [("BORROW", "978-Z")])
    assert catalog == {"978-A": 2}

def test_multiple_borrows():
    catalog = {"978-A": 5}
    process_actions(catalog, [("BORROW", "978-A"), ("BORROW", "978-A"), ("BORROW", "978-A")])
    assert catalog["978-A"] == 2

def test_borrow_and_return_net_zero():
    catalog = {"978-A": 2}
    process_actions(catalog, [("BORROW", "978-A"), ("RETURN", "978-A")])
    assert catalog["978-A"] == 2

def test_empty_actions_catalog_unchanged():
    catalog = {"978-A": 3, "978-B": 1}
    process_actions(catalog, [])
    assert catalog == {"978-A": 3, "978-B": 1}

def test_multiple_books_only_target_affected():
    catalog = {"978-A": 2, "978-B": 2}
    process_actions(catalog, [("BORROW", "978-A")])
    assert catalog["978-A"] == 1
    assert catalog["978-B"] == 2

def test_borrow_exhausts_all_copies():
    catalog = {"978-A": 2}
    process_actions(catalog, [("BORROW", "978-A"), ("BORROW", "978-A"), ("BORROW", "978-A")])
    assert catalog["978-A"] == 0

def test_returns_catalog():
    catalog = {"978-A": 1}
    result = process_actions(catalog, [("BORROW", "978-A")])
    assert result == {"978-A": 0}
