@echo off
pyinstaller --onefile main.py -n jeveasset_sp.exe
rd /s /q .\build