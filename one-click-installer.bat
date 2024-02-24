@echo off
SET venv_dir=venv
SET repo_url=https://github.com/samfisherirl/PySimpleGUI-Bypass-Login-Remove-Ad/archive/master.zip
SET repo_zip=PySimpleGUI-Bypass-Login-Remove-Ad-master.zip

REM Check if the virtual environment directory exists
IF EXIST "%venv_dir%\Scripts\activate.bat" (
    ECHO Virtual environment found. Activating...
) ELSE (
    ECHO Creating virtual environment...
    python -m venv %venv_dir%
)

REM Activate the virtual environment
CALL %venv_dir%\Scripts\activate.bat

REM Download the repository zip file
powershell -command "Invoke-WebRequest -Uri %repo_url% -OutFile %repo_zip%"

REM Unzip the repository zip file
powershell -command "Expand-Archive -Path %repo_zip% -DestinationPath ."

REM Upgrade pip and install requirements if needed
IF EXIST "%venv_dir%\Scripts\pip.exe" (
    ECHO Upgrading pip...
    python -m pip install --upgrade pip
    python -m pip install --upgrade -r PySimpleGUI-Bypass-Login-Remove-Ad-main\requirements.txt
)

REM Run the Python script
python PySimpleGUI-Bypass-Login-Remove-Ad-main\PySimpleGUI.py

REM close this window on completion

REM Pause the command window
pause
