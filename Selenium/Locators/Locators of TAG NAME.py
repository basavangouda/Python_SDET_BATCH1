#Script 1
#Locating an element with Tag Name
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("file:///D:/Python_SDET_March-2024-Batch/HTML/Sample%20TAG%20NAME%20File.html")
driver.maximize_window()
print(driver.find_element(By.TAG_NAME,"h1").text)
time.sleep(5)
driver.close()

#Script 2
#Locating an element with Tag Name
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.nykaa.com/")
driver.maximize_window()
#To find single element we use below line
print(driver.find_element(By.TAG_NAME,"a").text)

print("*********************************************")
#To find list of elements we use below line
links=driver.find_elements(By.TAG_NAME,"a")
for x in links:
    print(x.text)
time.sleep(5)
driver.close()

#Script 3
#Locating an element with Tag Name
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("file:///D:/Python_SDET_March-2024-Batch/HTML/Class%20Name%20Locator.html")
driver.maximize_window()
print(driver.find_element(By.TAG_NAME,"p").text)
time.sleep(5)
driver.close()