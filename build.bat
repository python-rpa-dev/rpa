pipenv run pyinstaller --onefile rpa.py --distpath .
del rpa.zip
7z a rpa.zip rpa.exe rpa.ini launch_rpa.bat tmp\*.*