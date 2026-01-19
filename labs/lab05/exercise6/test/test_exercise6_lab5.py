import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise6.py')
_spec = importlib.util.spec_from_file_location("exercise6_lab5", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
find_slow_endpoints = _module.find_slow_endpoints


def test_basic_slow_endpoints():
    api_calls = [
        ("/login", 45, 200), 
        ("/login", 120, 200), 
        ("/data", 80, 200),
        ("/data", 95, 200)
    ]
    assert find_slow_endpoints(api_calls, 70) == ["/data", "/login"]


def test_with_error_status():
    api_calls = [
        ("/login", 45, 200), 
        ("/login", 120, 200),
        ("/login", 50, 500),
        ("/data", 80, 200),
        ("/data", 95, 200)
    ]
    assert find_slow_endpoints(api_calls, 70) == ["/data", "/login"]


def test_single_call_excluded():
    api_calls = [
        ("/login", 45, 200), 
        ("/login", 120, 200),
        ("/search", 30, 200),
        ("/health", 150, 200)
    ]
    assert find_slow_endpoints(api_calls, 70) == ["/login"]


def test_no_slow_endpoints():
    api_calls = [
        ("/api1", 20, 200), 
        ("/api1", 30, 200),
        ("/api2", 40, 200),
        ("/api2", 50, 200)
    ]
    assert find_slow_endpoints(api_calls, 100) == []


def test_all_slow_endpoints():
    api_calls = [
        ("/slow1", 100, 200), 
        ("/slow1", 120, 200),
        ("/slow2", 110, 200),
        ("/slow2", 130, 200)
    ]
    assert find_slow_endpoints(api_calls, 50) == ["/slow1", "/slow2"]


def test_threshold_boundary():
    api_calls = [
        ("/exact", 70, 200), 
        ("/exact", 70, 200),
        ("/over", 71, 200),
        ("/over", 71, 200)
    ]
    assert find_slow_endpoints(api_calls, 70) == ["/over"]


def test_multiple_endpoints():
    api_calls = [
        ("/api1", 50, 200),
        ("/api1", 100, 200),
        ("/api2", 60, 200),
        ("/api2", 80, 200),
        ("/api3", 30, 200),
        ("/api3", 40, 200)
    ]
    assert find_slow_endpoints(api_calls, 65) == ["/api1", "/api2"]


def test_alphabetical_sorting():
    api_calls = [
        ("/zebra", 100, 200),
        ("/zebra", 120, 200),
        ("/apple", 90, 200),
        ("/apple", 110, 200)
    ]
    assert find_slow_endpoints(api_calls, 70) == ["/apple", "/zebra"]


def test_mixed_status_codes():
    api_calls = [
        ("/api", 50, 200),
        ("/api", 100, 200),
        ("/api", 200, 404),
        ("/api", 80, 200)
    ]
    assert find_slow_endpoints(api_calls, 70) == ["/api"]


def test_three_successful_calls():
    api_calls = [
        ("/endpoint", 60, 200),
        ("/endpoint", 80, 200),
        ("/endpoint", 100, 200)
    ]
    assert find_slow_endpoints(api_calls, 75) == ["/endpoint"]
