import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise4.py')
_spec = importlib.util.spec_from_file_location("exercise4_lab7", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
apply_upgrade = _module.apply_upgrade


def test_higher_level_applied():
    current = {"write": 1}
    result = apply_upgrade(current, {"write": 3})
    assert result["write"] == 3

def test_lower_level_not_applied():
    current = {"read": 2}
    result = apply_upgrade(current, {"read": 1})
    assert result["read"] == 2

def test_new_permission_added():
    current = {"read": 2}
    result = apply_upgrade(current, {"execute": 2})
    assert result["execute"] == 2

def test_original_current_unchanged():
    current = {"read": 2, "write": 1}
    apply_upgrade(current, {"write": 3})
    assert current == {"read": 2, "write": 1}

def test_equal_level_not_applied():
    current = {"read": 2}
    result = apply_upgrade(current, {"read": 2})
    assert result["read"] == 2

def test_empty_current_all_upgrade_added():
    result = apply_upgrade({}, {"read": 1, "write": 2})
    assert result == {"read": 1, "write": 2}

def test_empty_upgrade_returns_copy_of_current():
    current = {"read": 2, "admin": 0}
    result = apply_upgrade(current, {})
    assert result == {"read": 2, "admin": 0}

def test_unaffected_permissions_preserved():
    current = {"read": 2, "write": 1, "admin": 0}
    result = apply_upgrade(current, {"write": 3})
    assert result["read"] == 2
    assert result["admin"] == 0

def test_full_example():
    current = {"read": 2, "write": 1, "admin": 0}
    upgrade = {"read": 1, "write": 3, "execute": 2}
    result = apply_upgrade(current, upgrade)
    assert result == {"read": 2, "write": 3, "admin": 0, "execute": 2}

def test_zero_level_added_as_new_permission():
    current = {"read": 2}
    result = apply_upgrade(current, {"new_perm": 0})
    assert "new_perm" in result
    assert result["new_perm"] == 0
