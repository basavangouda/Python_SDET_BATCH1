@echo off
:: Navigate to project directory
cd /d D:\Python_SDET_March-2024-Batch\Selenium\Selenium_Methods

:: Set up virtual environment
python -m venv venv
call venv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt

:: Run Python script
python Date_Picker.py
python Drop_Down.py

