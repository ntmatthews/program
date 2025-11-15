@echo off
setlocal enableextensions enabledelayedexpansion
cd /d %~dp0\..\..

py -m pip install --upgrade pip wheel setuptools >NUL
py -m pip install -r requirements-dev.txt

py -m PyInstaller --clean --noconfirm --onefile --windowed --name PortableDB portable_database.py

echo Built Windows binary at: dist\PortableDB.exe
