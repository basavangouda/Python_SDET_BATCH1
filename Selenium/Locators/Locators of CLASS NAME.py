#Script 1
#Locating an element with Class Name
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("file:///D:/Python_SDET_March-2024-Batch/HTML/Class%20Name%20Locator.html")
driver.maximize_window()
print(driver.find_element(By.CLASS_NAME,"content").text)
time.sleep(5)
driver.close()

#Script 2
#Locating an element with Class Name
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.nykaa.com/")
driver.maximize_window()
print(driver.find_element(By.CLASS_NAME,"css-1gzc5zn").text)
time.sleep(5)
driver.find_element(By.CLASS_NAME,"css-1gzc5zn").click()
time.sleep(5)
driver.close()