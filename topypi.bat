@echo off
REM Batchfile which send this library on PyPI
python -m build
twine upload dist/*
exit