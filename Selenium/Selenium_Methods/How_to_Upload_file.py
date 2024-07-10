import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

#Example 1 Chrome Browser

#driver = webdriver.Chrome()
driver=webdriver.Firefox()
#driver=webdriver.Edge()
driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
driver.maximize_window()
time.sleep(5)

upload_file=driver.find_element(By.ID,"uploadFile")
upload_file.send_keys("C:\\Users\\dell\\Desktop\\csv_sample.csv")
time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(5)
driver.quit()