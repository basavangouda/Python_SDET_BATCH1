#Chrome
import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://mamaearth.in/")
driver.maximize_window()
Exp_Result="Mamaearth Summer Sale is Live! Buy 3 Pay For 2"
Act_Result=driver.title
print(Act_Result)

if Act_Result==Exp_Result:
    print("Test Pass")
else:
    print("Test Fail")
driver.close()

#Mozilla FireFox
import time
from selenium import webdriver
#from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.firefox.options import Options
#option=Options()
#option.binary_location="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
#service_obj=Service("C:\\Driver\\geckodriver.exe")
#driver=webdriver.Firefox(service=service_obj,options=option)
driver=webdriver.Firefox()
driver.get("https://mamaearth.in/")
driver.maximize_window()
Exp_Result="Mamaearth Summer Sale is Live! Buy 3 Pay For 2"
Act_Result=driver.title

if Act_Result==Exp_Result:
    print("Test Pass")
else:
    print("Test Fail")
driver.close()

#Edge
import time
from selenium import webdriver

#from selenium.webdriver.edge.service import Service
#service_obj=Service("C:\\Driver\\msedgedriver.exe")
#driver=webdriver.Edge(service=service_obj)

driver=webdriver.Edge()
driver.get("https://mamaearth.in/")
driver.maximize_window()
Exp_Result="Mamaearth Summer Sale is Live! Buy 3 Pay For 2"
Act_Result=driver.title

if Act_Result==Exp_Result:
    print("Test Pass")
else:
    print("Test Fail")
driver.close()