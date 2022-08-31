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
git clone https://github.com/python-rpa-dev/rpa.git
cd rpa
pipenv shell
pip install -r requirements.txt
```

## New: Run RPA client as binary (Windows only, for now)

* Download rpa.zip from github folder
* Unzip to a folder of your choice.
* Launch Browser, either Firefox or Chrome and log into the application, make sure that the browser window is not covered by other window/applications
* Open command line console, like terminator (sandbox) / cmd.exe (windows desktop) and change to the folder
* Run the following command

```
launch_rpa
```

If you want to use a different profile, as in the following section (RPA_test, ...) you can 

* copy and modify launch_rpa.pat in the same directory
* or open command line console, like terminator (sandbox) / cmd.exe (windows desktop), switch to the directory and run

```
rpa.exe --ini-file rpa.ini --profile RPA_std
```

## Run RPA client on sandbox or desktop

* Connect to GUI via VirtualBox, use vagrant to login. You don't need this step for your desktop.
* Launch Browser, either Firefox or Chrome and log into the application, make sure that the browser window is not covered by other window/applications
* Open command line console, like terminator (sandbox) / cmd.exe (windows desktop)

```
cd rpa
pipenv run python rpa.py --ini-file rpa.ini --profile RPA_std
```

Available profiles are:
- RPA_test -> Tests one GUI element
- RPA_std -> Default tasks
- RPA_ext -> Default tasks + experimental/new tasks
