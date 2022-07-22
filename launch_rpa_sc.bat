@REM Launch RPA client
SET RPA_LOGLEVEL=INFO
pipenv run python rpa.py --ini-file rpa.ini --profile RPA_sc
Pause
