#!/bin/bash

python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip install --prefer-binary -r requirements.txt

pytest -s tests