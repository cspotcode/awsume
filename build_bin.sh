#!/usr/bin/env bash
set -euo pipefail
shopt -s inherit_errexit

# echo 'This script has become a guide, not an executable script, cuz it needs to'
# echo 'happen inside pipenv shell and I havent updated it for that'
# # exit 1

# Install deps and create virtualenv
pipenv install --dev

# To do things in the pipenv, get a shell:
# pipenv shell

# Build binary
pipenv run nuitka3 \
    --standalone --onefile \
    --output-filename=awsumepy \
    ./bin_entrypoint.py
