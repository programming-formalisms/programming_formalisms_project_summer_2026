#!/bin/bash
#
# Upload this package to TestPyPI
#
# Usage:
#
#   ./scripts/upload_this_package_to_testpypi.sh
#
#
#
if [[ "$PWD" =~ scripts$ ]]; then
    echo "Please run the script from the project root. "
    echo "Present working director: $PWD"
    echo " "
    echo "Tip: like this"
    echo " "
    echo "./scripts/upload_this_package_to_testpypi.sh"
    exit 42
fi

python3 -m twine upload --repository testpypi dist/*
