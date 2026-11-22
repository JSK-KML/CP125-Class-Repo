import importlib.util
import os
import threading

import pytest

EXERCISE = "exercise3"
FUNCTION = "validate_entry"
PARAMETERS = ['name', 'pin']
TIME_LIMIT = 10  # seconds, so a loop that never ends cannot freeze the tests

_state = {}


def run_with_time_limit(task, what):
    result = {}

    def target():
        try:
            result["value"] = task()
        except BaseException as error:
            result["error"] = error

    thread = threading.Thread(target=target, daemon=True)
    thread.start()
    thread.join(TIME_LIMIT)
    if thread.is_alive():
        message = f"{what} took too long (over {TIME_LIMIT} seconds) - check for a loop that never ends"
        _state["fail"] = message
        pytest.fail(message)
    if "error" in result:
        raise result["error"]
    return result.get("value")


def uses_input(error):
    return isinstance(error, OSError) and "reading from stdin" in str(error)


def load_function():
    if "fail" in _state:
        pytest.fail(_state["fail"])
    if "function" in _state:
        return _state["function"]

    def stop(message):
        _state["fail"] = message
        pytest.fail(message)

    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), EXERCISE + ".py")
    if not os.path.isfile(path):
        stop(f"{EXERCISE}.py was not found in the {EXERCISE} folder")
    spec = importlib.util.spec_from_file_location("lab01_" + EXERCISE, path)
    module = importlib.util.module_from_spec(spec)
    try:
        run_with_time_limit(lambda: spec.loader.exec_module(module), EXERCISE + ".py")
    except Exception as error:
        if uses_input(error):
            stop(f"{EXERCISE}.py uses input() - remove it, the tests give your function its values")
        stop(f"{EXERCISE}.py did not run: {type(error).__name__}: {error}")
    if not callable(getattr(module, FUNCTION, None)):
        stop(f"no function called {FUNCTION} in {EXERCISE}.py - check the name in your def line")
    _state["function"] = getattr(module, FUNCTION)
    return _state["function"]


CASES = [
    (('Director', 1122), True),
    (('Security', 9900), True),
    (('Director', 9900), False),
    (('Security', 1122), False),
    (('Admin', 1122), False),
    (('director', 1122), False),
    (('Director ', 1122), False),
    (('SECURITY', 9900), False),
    (('', 0), False),
    (('Hacker', 1234), False),
]


@pytest.mark.parametrize("args,expected", CASES)
def test_validate_entry(args, expected):
    function = load_function()
    context = "input " + ", ".join(f"{name}={value!r}" for name, value in zip(PARAMETERS, args))
    try:
        actual = run_with_time_limit(lambda: function(*args), f"{context} -> the function")
    except TypeError as error:
        if FUNCTION + "()" in str(error):
            pytest.fail(f"{context} -> the function could not be called: {error}")
        pytest.fail(f"{context} -> the function crashed: TypeError: {error}")
    except Exception as error:
        if uses_input(error):
            pytest.fail(f"{FUNCTION} uses input() - remove it, the values come from the parameters")
        pytest.fail(f"{context} -> the function crashed: {type(error).__name__}: {error}")
    hint = " (did you forget to return the result?)" if actual is None else ""
    assert actual == expected, f"{context} -> expected {expected!r} but got {actual!r}{hint}"
