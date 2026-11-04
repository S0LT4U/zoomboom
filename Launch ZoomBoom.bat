@echo off
rem Serves this folder at http://localhost:8777 so YouTube will play (it blocks pages opened as plain files).
cd /d "%~dp0"
start "" http://localhost:8777/index.html
echo ZoomBoom is running at http://localhost:8777/index.html  -  close this window to stop.
python -m http.server 8777 --bind 127.0.0.1
