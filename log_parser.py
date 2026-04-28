"""Parse pytest verbose output into per-test results."""

import re


def parse_log(log: str) -> dict[str, str]:
    """Parse test runner output into per-test results.

    Args:
        log: Full stdout+stderr output of `bash run_test.sh 2>&1`.

    Returns:
        Dict mapping test_id to status.
        - test_id: pytest native format (e.g. "tests/foo.py::TestClass::test_func[param]")
        - status: one of "PASSED", "FAILED", "SKIPPED", "ERROR"
        - Must include ALL tests that appear in the output, not just failures.
    """
    results: dict[str, str] = {}
    # Strip ANSI escape codes
    log = re.sub(r"\x1b\[[0-9;]*m", "", log)

    for line in log.splitlines():
        line = line.strip()

        # --- pytest-xdist format: [gwN] [ XX%] STATUS test_id ---
        m = re.match(
            r"\[gw\d+\]\s+\[\s*\d+%\]\s+(PASSED|FAILED|SKIPPED|ERROR|XFAIL)\s+(\S+::\S+.*)",
            line,
        )
        if m:
            status = m.group(1)
            test_id = m.group(2).strip()
            if status == "XFAIL":
                status = "SKIPPED"
            results.setdefault(test_id, status)
            continue

        # --- Standard verbose: test_id STATUS [ XX%] ---
        # Match from start: path::something ... STATUS [ XX%]
        # The test_id can contain brackets and spaces (parametrized tests)
        # so we anchor on the trailing STATUS + [ XX%]
        m = re.match(
            r"^(\S+::\S+.*?)\s+(PASSED|FAILED|SKIPPED|ERROR|XFAIL)\s+\[\s*\d+%\]",
            line,
        )
        if m:
            test_id = m.group(1).strip()
            status = m.group(2)
            if status == "XFAIL":
                status = "SKIPPED"
            results.setdefault(test_id, status)
            continue

        # --- Summary section: FAILED test_id - message ---
        m = re.match(r"^(PASSED|FAILED|SKIPPED|ERROR)\s+(\S+::\S+)", line)
        if m:
            status = m.group(1)
            test_id = m.group(2).strip()
            results.setdefault(test_id, status)
            continue

        # --- Collection errors: ERROR tests/foo.py (no ::) ---
        m = re.match(r"^ERROR\s+(tests/\S+\.py)\s*", line)
        if m and "::" not in m.group(1):
            test_id = m.group(1)
            results.setdefault(test_id, "ERROR")
            continue

    return results

