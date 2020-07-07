#!/bin/bash

echo 'setting up python virtualenv'
virtualenv --python=`which python3` .venv

echo 'installing dev requirements'
source .venv/bin/activate
pip install -r requirements.txt
pip install -r test-requirements.txt

echo 'setup is done'
echo 'please run `source .venv/bin/activate` in your current shell'
echo 'to use the correct python interpreter and packages'
