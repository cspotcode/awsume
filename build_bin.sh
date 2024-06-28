#!/usr/bin/env bash
set -euo pipefail
shopt -s inherit_errexit

# Ensure venv
python -m venv .venv
source .venv/bin/activate

# Install deps
pipenv install --dev

# Build binary
nuitka3 \
    --standalone --onefile \
    --output-filename=awsumepy \
    ./bin_entrypoint.py
