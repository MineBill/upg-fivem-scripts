#! /bin/sh

if [[ $# -lt 1 ]]; then
    echo "No veriables file was given"
    echo "Exiting..."
    exit 2
fi

echo "Generating configs from definitions.."
python3 scripts/merger.py configs/
echo "Done"
echo "Replacing all veriables"
python3 var_replace.py ${1}
echo "Done"