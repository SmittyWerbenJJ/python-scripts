@echo off
REM This batch file will start the python-scripts-gui

REM check if venv python executable exists, if it doesent exist,create it
if not exist .venv\scripts\python.exe (
    echo Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 (
        echo Failed to create virtual environment. Have you installed Python?
        goto :end
    )
)

echo Activating virtual environment...
call .venv/scripts/activate.bat

echo Installing requirements...
call pip install -r requirements.txt -q

echo Launching Program...
call python python_scripts_gui.py
pause
