@echo off
REM Portable Database Launcher for Windows
REM Double-click this file to run the database

cd /d "%~dp0"

echo.
echo ============================================
echo   🗄️  Portable Database System
echo ============================================
echo.

REM Check if Python 3 is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed!
    echo Please install Python 3 from python.org
    echo.
    pause
    exit /b 1
)

REM Run the portable database
echo Starting database...
echo.
python portable_database.py

REM Keep window open if there's an error
if %errorlevel% neq 0 (
    echo.
    echo An error occurred!
    pause
)
