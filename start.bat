@echo off

if not exist "%~dp0frontend/node_modules" (
    start "NodeModulesInstall" cmd /k "cd /d %~dp0frontend && npm i"
)

if not exist "%~dp0backend/venv" (
    start "PythonModulesInstall" cmd /k "cd /d %~dp0backend && venv\Scripts\activate && pip install -r requirements.txt"
)

start "Backend" cmd /k "cd /d %~dp0backend && venv\Scripts\activate && python manage.py runserver"
start "Frontend" cmd /k "cd /d %~dp0frontend && npm start"

exit