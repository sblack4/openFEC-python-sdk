#!/bin/bash

virtualenv --python=`which python3` .venv

.venv/bin/activate

pip install -r requirements.txt
