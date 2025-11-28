@echo off
REM Script which send this library on PyPI

REM Deleting sending cache directories
rmdir dist /s /q
rmdir msound.egg-info /s /q

REM Sending to PyPI
python -m build
twine upload dist/*

exit
