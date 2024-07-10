#Script 1
#Locating an element with Partial Link Text
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("file:///D:/Python_SDET_March-2024-Batch/HTML/Link%20Text%20Locator%20HTML.html")
driver.maximize_window()
print(driver.find_element(By.PARTIAL_LINK_TEXT,"Can").text)
time.sleep(5)
driver.find_element(By.PARTIAL_LINK_TEXT,"Can").click()
time.sleep(5)
driver.close()

#Script 2
#Locating an element with Partial Link Text
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.selenium.dev/downloads/")
driver.maximize_window()
print(driver.find_element(By.PARTIAL_LINK_TEXT,"Proj").text)
time.sleep(5)
driver.find_element(By.PARTIAL_LINK_TEXT,"Proj").click()
time.sleep(5)
driver.close()