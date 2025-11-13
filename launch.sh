#!/bin/bash
# Portable Database Launcher for Mac/Linux
# Double-click this file to run the database

cd "$(dirname "$0")"

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed!"
    echo "Please install Python 3 from python.org"
    read -p "Press Enter to exit..."
    exit 1
fi

# Run the portable database
echo "🗄️  Starting Portable Database..."
python3 portable_database.py

# Keep window open if there's an error
if [ $? -ne 0 ]; then
    read -p "Press Enter to exit..."
fi
