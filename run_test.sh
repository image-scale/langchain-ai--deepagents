#!/bin/bash
set -eo pipefail

export PYTHONDONTWRITEBYTECODE=1
export PYTHONUNBUFFERED=1
export CI=true

REPO_ROOT=/workspace/deepagents
EXIT_CODE=0

run_tests() {
  local dir="$1"
  shift
  cd "$REPO_ROOT/$dir"
  rm -rf .pytest_cache
  uv run pytest "$@" || EXIT_CODE=1
}

# --- deepagents (core SDK) ---
run_tests libs/deepagents tests/unit_tests/ \
  -v --tb=short --no-cov --no-header \
  --disable-socket --allow-unix-socket \
  -p no:cacheprovider --benchmark-disable \
  --timeout=30

# --- deepagents-cli ---
run_tests libs/cli tests/unit_tests/ \
  -v --tb=short --no-cov --no-header \
  --disable-socket --allow-unix-socket \
  -p no:cacheprovider --benchmark-disable \
  --timeout=30

# --- deepagents-acp ---
run_tests libs/acp tests/ \
  -v --tb=short --no-cov --no-header \
  --disable-socket --allow-unix-socket \
  -p no:cacheprovider \
  --timeout=30

# --- langchain-quickjs ---
run_tests libs/partners/quickjs tests/unit_tests/ \
  -v --tb=short --no-cov --no-header \
  --disable-socket --allow-unix-socket \
  -p no:cacheprovider \
  --timeout=30

# --- langchain-daytona ---
run_tests libs/partners/daytona tests/unit_tests/ \
  -v --tb=short --no-cov --no-header \
  --disable-socket --allow-unix-socket \
  -p no:cacheprovider \
  --timeout=30

# --- langchain-modal ---
run_tests libs/partners/modal tests/unit_tests/ \
  -v --tb=short --no-cov --no-header \
  --disable-socket --allow-unix-socket \
  -p no:cacheprovider \
  --timeout=30

# --- langchain-runloop ---
run_tests libs/partners/runloop tests/unit_tests/ \
  -v --tb=short --no-cov --no-header \
  --disable-socket --allow-unix-socket \
  -p no:cacheprovider \
  --timeout=30

exit $EXIT_CODE

