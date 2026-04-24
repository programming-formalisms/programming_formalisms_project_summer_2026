#!/bin/bash
#
# Install the package from the local code
#
# Usage:
#
#   ./scripts/install_this_package.sh
#
#
#
if [[ "$PWD" =~ scripts$ ]]; then
    echo "Please run the script from the project root. "
    echo "Present working director: $PWD"
    echo " "
    echo "Tip: like this"
    echo " "
    echo "./scripts/install_this_package.sh"
    exit 42
fi

python3 -m pip install . --break-system-packages
