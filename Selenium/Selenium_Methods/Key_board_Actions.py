"""
1. Open an application :https://text-compare.com/
2. Go to first text field and enter the text "Welcome to QACircle"
3. Same text copy and past it in second text field

"""
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://text-compare.com/")
driver.maximize_window()

#Find the xpath of two text fields
input1=driver.find_element(By.ID,"inputText1")
input2=driver.find_element(By.ID,"inputText2")

input1.send_keys("Welcome to QACircle")
time.sleep(5)

act=ActionChains(driver)

#Selecting the text
# act.key_down(Keys.CONTROL)
# act.send_keys('a')
# act.key_up(Keys.CONTROL)
# act.perform()

#We can write whole script in oneline
act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

#Copy the text
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

#Press tab to navigate to second text field
act.send_keys(Keys.TAB).perform()

time.sleep(5)
#input2.send_keys(Keys.CONTROL,'v')
#act.key_down(Keys.CONTROL).send_keys('v').perform()

time.sleep(5)
driver.close()


