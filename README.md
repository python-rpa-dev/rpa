# Another try at RPA bot 

## Setup

* Log into sandbox: vagrant ssh 
* Optional: create rpa user or use vagrant user of the sandbox 

```
git clone https://github.com/python-rpa-dev/rpa.git
cd rpa
pipenv shell
pip install opencv-python pyautogui imutils pillow
```

## Run RPA prototype

* Connect to GUI via VirtualBox, use vagrant to login.
* Launch Browser, either Firefox or Chrome and log into the application
* Open command line console, like terminator

```
cd rpa
pipenv run python rpa.py
```

