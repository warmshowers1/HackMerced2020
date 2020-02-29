#!/bin/bash

python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt

printf "Make sure to run: source venv/bin/activate !!!\n"
