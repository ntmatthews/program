#!/usr/bin/env zsh
set -euo pipefail

SCRIPT_DIR=${0:a:h}
PROJECT_ROOT=${SCRIPT_DIR:h:h}
cd "$PROJECT_ROOT"

python3 -m pip install --upgrade pip wheel setuptools >/dev/null
python3 -m pip install -r requirements-dev.txt

pyinstaller --clean --noconfirm --onefile --windowed --name PortableDB portable_database.py

echo "Built macOS single-file binary at: dist/PortableDB"
