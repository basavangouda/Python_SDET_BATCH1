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
python Find_Broken_Images.py
python Handling Alerts.py
python Handling Cookies.py
python python Handling Frames.py
python Handling Mouse_Hover_Actions.py
python Handling Table.py
python Handling Windows.py   
python Handling_Bootstrap_dropdown.py   
python Headless Mode Testing.py
python How_to_take_Screenshot.py        
python Open_QACirle_Courses_Page_Key_Actions.py



