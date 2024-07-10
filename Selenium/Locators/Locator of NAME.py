#Script 1
#Locating an element with Name
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.NAME,"user-name").send_keys("QACircle")
time.sleep(5)
driver.close()

#Script 2
#Locating an element with Name
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.linkedin.com/login")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.NAME,"session_key").send_keys("QACircle")
time.sleep(5)
driver.close()

#Script 3
#Locating an element with Name
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("file:///D:/Python_SDET_March-2024-Batch/HTML/Basic%20Loginpage_Name%20Locator.html")
driver.maximize_window()
time.sleep(5)

username=driver.find_element(By.NAME,"uname")
username.send_keys("Hello")
password=driver.find_element(By.NAME,"psw")
password.send_keys("Hello")

time.sleep(5)
driver.close()
