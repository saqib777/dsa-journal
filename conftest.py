# Root conftest.py for dsa-journal
# Shared pytest configuration, fixtures, and hooks

import pytest
import time
import os
from datetime import datetime


# ── Session-level fixtures ─────────────────────────────────────────────────────

@pytest.fixture(scope="session")
def test_start_time():
    """Record session start time for duration reporting."""
    return datetime.now()


# ── Timing fixture ─────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def track_test_time(request):
    """
    Auto-applied fixture that tracks how long each test takes.
    Prints duration after each test in verbose mode.
    """
    start = time.time()
    yield
    duration = time.time() - start
    if duration > 1.0:
        print(f"\n  [SLOW] {request.node.name} took {duration:.2f}s")


# ── Markers ────────────────────────────────────────────────────────────────────

def pytest_configure(config):
    """Register custom markers to avoid warnings."""
    config.addinivalue_line("markers", "slow: mark test as slow running")
    config.addinivalue_line("markers", "easy: LeetCode easy difficulty")
    config.addinivalue_line("markers", "medium: LeetCode medium difficulty")
    config.addinivalue_line("markers", "hard: LeetCode hard difficulty")
    config.addinivalue_line("markers", "arrays: array category problems")
    config.addinivalue_line("markers", "strings: string category problems")
    config.addinivalue_line("markers", "trees: tree category problems")
    config.addinivalue_line("markers", "graphs: graph category problems")
    config.addinivalue_line("markers", "dp: dynamic programming problems")
    config.addinivalue_line("markers", "linked_lists: linked list problems")


# ── Summary hook ───────────────────────────────────────────────────────────────

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Print custom summary at end of test run."""
    passed  = len(terminalreporter.stats.get('passed',  []))
    failed  = len(terminalreporter.stats.get('failed',  []))
    skipped = len(terminalreporter.stats.get('skipped', []))
    total   = passed + failed + skipped

    print(f"\n{'='*55}")
    print(f"  DSA Journal Test Summary")
    print(f"  Total:   {total}")
    print(f"  Passed:  {passed}  |  Failed: {failed}  |  Skipped: {skipped}")
    print(f"  Run at:  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*55}")
