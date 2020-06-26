#/bin/bash

rm -rf ./build
rm -rf ./dist
rm -rf ./*.egg-info
rm -rf ./venv
python3 -m venv ./venv
source venv/bin/activate
pip3 install setuptools==38.5.2
pip3 install twine==1.10.0
pip3 install wheel==0.30.0
python3 setup.py clean --all bdist_wheel 
twine upload -r kingpypi --config-file ./twine.cfg ./dist/*.whl
