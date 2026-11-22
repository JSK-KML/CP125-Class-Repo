"""Shared pytest configuration for every lab.

Keeps the output clean: students see only whether every test passed, or a
short "expected X but got Y" line per failure, never a Python stack trace.

It sits at the root of the repository so pytest always loads it first, also
when VS Code runs every test from the root.
"""

import pytest


# Exercises that are not in the lab page yet. Remove a line to bring one back.
collect_ignore = [
    "labs/lab01/exercise7",
    "labs/lab01/exercise8",
    "labs/lab01/exercise9",
    "labs/lab01/exercise10",
    "labs/lab01/exercise11",
    "labs/lab01/exercise12",
    "labs/lab01/exercise13",
    "labs/lab01/exercise14",
]


def pytest_configure(config):
    # Silence tracebacks and the noisy default reporting.
    config.option.tbstyle = "no"
    config.option.verbose = -1
    # Drop pytest's own "short test summary info" (the FAILED ... list),
    # so students only see our tidy result block below.
    config.option.reportchars = ""


# The clean, one-line reason for each failing test, without repeats.
_failures = []


def _clean(report):
    crash = getattr(report.longrepr, "reprcrash", None)
    message = crash.message if crash else str(report.longrepr or "test failed")
    clean = message.strip().splitlines()[0] if message.strip() else "test failed"
    for prefix in ("AssertionError:", "Failed:"):
        if clean.startswith(prefix):
            clean = clean[len(prefix):].strip()
    return clean


def _add(line):
    if line not in _failures:
        _failures.append(line)


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    if report.failed and report.when in ("setup", "call"):
        _add(_clean(report))


@pytest.hookimpl(tryfirst=True)
def pytest_collectreport(report):
    # A test file that cannot even be loaded must not end in "ALL TESTS PASSED".
    if report.failed:
        _add(_clean(report))


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    # Replace pytest's default summary with our own tidy result block.
    if config.option.collectonly:
        return  # VS Code only listing the tests: nothing has run yet.
    terminalreporter.line("")
    if _failures:
        terminalreporter.line("SOME TESTS FAILED:")
        for line in _failures:
            terminalreporter.line(f"  - {line}")
    elif exitstatus == pytest.ExitCode.NO_TESTS_COLLECTED:
        terminalreporter.line("NO TESTS FOUND")
    else:
        terminalreporter.line("ALL TESTS PASSED")
