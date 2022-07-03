#!/usr/bin/env bash
export RPA_LOGLEVEL=INFO
export DISPLAY=:0 
pipenv run python rpa.py --ini-file rpa.ini
