#!/bin/bash
#
# Run the unittest tests.
#
# Usage:
#
#   ./scripts/run_tests.sh

if [[ "$PWD" =~ scripts$ ]]; then
    echo "Please run the script from the project root. "
    echo "Present working director: $PWD"
    echo " "
    echo "Tip: like this"
    echo " "
    echo "./scripts/run_tests.sh"
    exit 42
fi

python -m unittest discover
