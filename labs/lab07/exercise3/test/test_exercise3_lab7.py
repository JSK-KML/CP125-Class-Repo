import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise3.py')
_spec = importlib.util.spec_from_file_location("exercise3_lab7", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
compare_prices = _module.compare_prices


def test_basic_comparison():
    a = {"milk": 3.50, "bread": 2.00, "eggs": 5.00, "butter": 4.50}
    b = {"milk": 3.00, "bread": 2.50, "eggs": 5.00, "coffee": 8.00}
    result = compare_prices(a, b)
    assert result["only_a"] == ["butter"]
    assert result["a_cheaper"] == ["bread"]
    assert result["b_cheaper"] == ["milk"]

def test_equal_prices_not_in_any_list():
    a = {"eggs": 5.00}
    b = {"eggs": 5.00}
    result = compare_prices(a, b)
    assert result["only_a"] == []
    assert result["a_cheaper"] == []
    assert result["b_cheaper"] == []

def test_only_in_a():
    a = {"butter": 4.50}
    b = {}
    result = compare_prices(a, b)
    assert result["only_a"] == ["butter"]
    assert result["a_cheaper"] == []

def test_only_in_b_not_tracked():
    a = {}
    b = {"coffee": 8.00}
    result = compare_prices(a, b)
    assert result == {"only_a": [], "a_cheaper": [], "b_cheaper": []}

def test_a_always_cheaper():
    a = {"x": 1.00, "y": 2.00}
    b = {"x": 5.00, "y": 6.00}
    result = compare_prices(a, b)
    assert result["a_cheaper"] == ["x", "y"]
    assert result["b_cheaper"] == []

def test_b_always_cheaper():
    a = {"x": 5.00, "y": 6.00}
    b = {"x": 1.00, "y": 2.00}
    result = compare_prices(a, b)
    assert result["b_cheaper"] == ["x", "y"]
    assert result["a_cheaper"] == []

def test_empty_store_a():
    result = compare_prices({}, {"milk": 3.00})
    assert result == {"only_a": [], "a_cheaper": [], "b_cheaper": []}

def test_result_is_sorted():
    a = {"zebra": 1.00, "apple": 2.00, "mango": 1.50}
    b = {"zebra": 2.00, "apple": 3.00, "mango": 2.50}
    result = compare_prices(a, b)
    assert result["a_cheaper"] == ["apple", "mango", "zebra"]

def test_returns_three_keys():
    result = compare_prices({}, {})
    assert set(result.keys()) == {"only_a", "a_cheaper", "b_cheaper"}

def test_mixed_all_categories():
    a = {"a": 1.00, "b": 5.00, "c": 3.00}
    b = {"a": 2.00, "b": 3.00}
    result = compare_prices(a, b)
    assert result["only_a"] == ["c"]
    assert result["a_cheaper"] == ["a"]
    assert result["b_cheaper"] == ["b"]
