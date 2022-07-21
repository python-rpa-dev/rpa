# Another try at RPA client

## Setup

### Using your desktop
* Install python from the command line

```
winget install -e --id Python.Python.3
```

* Open another console and install pipenv

```
pip install pipenv

```

-> Continue with section *Installation*

### Using a sandbox
* Log into sandbox: vagrant ssh 
* Optional: create rpa user or use vagrant user of the sandbox

Note: The sandbox comes with an automated installation for the RPA client, the *Installation* step is only needed if you use another virtual machine setup.

### Installation 

* You need to select a folder where you want to install the RPA client. The users home directory is usually the default in the command line.

```
git clone https://github.com/Abiaz/rpa.git
cd rpa
pipenv shell
pip install opencv-python pyautogui imutils pillow
```

## Run RPA client on sandbox or desktop

* Connect to GUI via VirtualBox, use vagrant to login. You don't need this step for your desktop.
* Launch Browser, either Firefox or Chrome and log into the application
* Open command line console, like terminator (sandbox) / cmd.exe (windows desktop)

```
cd rpa
pipenv run python rpa.py --ini-file rpa.ini
```
