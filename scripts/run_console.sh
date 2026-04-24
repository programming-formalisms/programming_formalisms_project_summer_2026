#!/bin/bash
#
# Start a console application, by running 'main.py'
#
# Usage:
#
#   ./scripts/run_console.sh
#
#
#
if [[ "$PWD" =~ scripts$ ]]; then
    echo "Please run the script from the project root. "
    echo "Present working director: $PWD"
    echo " "
    echo "Tip: like this"
    echo " "
    echo "./scripts/run_console.sh"
    exit 42
fi

# Run the code
python3 main.py
