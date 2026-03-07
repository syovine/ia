#!/bin/bash

# Source the parent ia.sh to get Python path
source ../ia.sh

# Tell poetry to use the specific Python version
poetry env use $PYTHON

# Check if .venv exists, if not run poetry install
if [ ! -d ".venv" ]; then
    echo "Virtual environment not found. Running poetry install..."
    poetry install
fi

# Activate the virtual environment
source .venv/bin/activate

echo "Virtual environment activated. Python: $(which python)"
source .venv/bin/activate
