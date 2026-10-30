@echo off
rem Bam dup de mo Horror Video Studio (Windows)
cd /d "%~dp0"
set PYTHONUTF8=1
start "" http://localhost:8765
".venv\Scripts\python.exe" -W ignore tools\studio.py
