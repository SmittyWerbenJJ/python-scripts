@echo off
REM This batch file will start the python-scripts-gui
call .venv\Scripts\activate.bat
call pip install -r requirements.txt -q
call python python_scripts_gui.py
pause
