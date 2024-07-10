#Locators : Using Locators we can go and identify the web elements on the web page
"""
ID ='id'
NAME ='name'
CLASS_NAME='class name'
TAG_NAME='tag name'
LINK_TEXT='link text'
PARTIAL_LINK_TEXT='partial link text'
CSS_SELECTOR='css selector'
XPATH ='xpath'
"""

#find_element() ==> It will return the single element from the web page
#find_elements() ==>It will return the list of web elements from the web page

#Script 1
#Locating an element with ID
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.ID,"Attribute Value")
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
time.sleep(5)
driver.find_element(By.ID,"login-button").click()
time.sleep(5)
print(driver.title)
driver.close()

#Script 2
#Locating an element with ID
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.nykaa.com/")
driver.maximize_window()
time.sleep(5)
print(driver.find_element(By.ID,"category").text)
driver.find_element(By.ID,"category").click()
time.sleep(5)
driver.close()
