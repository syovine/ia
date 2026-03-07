#!/bin/bash

# Source the parent ia.sh to get Python path
source ../ia.sh

# Tell poetry to use the specific Python version
poetry env use $PYTHON

# Set poetry config
poetry config virtualenvs.in-project true

# poetry install
poetry install
echo "Virtual environment installed"

# Activate the virtual environment
source .venv/bin/activate
echo "Virtual environment activated. Python: $(which python)"
