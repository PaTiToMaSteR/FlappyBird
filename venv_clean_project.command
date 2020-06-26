#/bin/bash

rm -rf ./build
rm -rf ./dist
rm -rf ./*.egg-info
rm -rf ./venv
python -m venv ./venv
source venv/bin/activate
pip install setuptools
pip install wheel
