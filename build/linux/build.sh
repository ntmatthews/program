#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)
PROJECT_ROOT=$(dirname "$(dirname "$SCRIPT_DIR")")
cd "$PROJECT_ROOT"

python3 -m pip install --upgrade pip wheel setuptools >/dev/null
python3 -m pip install -r requirements-dev.txt

pyinstaller --clean --noconfirm --onefile --windowed --name PortableDB portable_database.py

echo "Built Linux binary at: dist/PortableDB"
