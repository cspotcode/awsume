#!/usr/bin/env bash
set -euo pipefail
shopt -s inherit_errexit

__dirname="$(CDPATH= cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$__dirname"

BIN_DIR=~/bin

rm "$BIN_DIR/awsume"
rm "$BIN_DIR/awsumepy"
rm "$BIN_DIR/awsume-configure"
rm "$BIN_DIR/autoawsume"
rm "$BIN_DIR/awsume-autocomplete"

ln -s "$PWD/shell_scripts/awsume" "$BIN_DIR/awsume"
ln -s "$PWD/awsumepy"             "$BIN_DIR/awsumepy"
ln -s "$PWD/awsumepy"             "$BIN_DIR/awsume-configure"
ln -s "$PWD/awsumepy"             "$BIN_DIR/autoawsume"
ln -s "$PWD/awsumepy"             "$BIN_DIR/awsume-autocomplete"
