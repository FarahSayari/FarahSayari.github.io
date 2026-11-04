@echo off
pushd "%~dp0.."
python "%~dp0generate.py"
popd
pause
