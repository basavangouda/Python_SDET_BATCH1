# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver import Keys
#
# #Example 1 Chrome Browser
# #Case 1
# driver = webdriver.Chrome()
# driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
# driver.maximize_window()
#
# #This code will download the file in default location
# driver.find_element(By.XPATH,"//button[normalize-space()='Download']").click()
# time.sleep(5)
# driver.close()
#
# #Case 2
# #Now my requirement is i want to download in my required location
# import os
# location=os.getcwd()
# options=webdriver.ChromeOptions()
# #prefs={"download.default_directory":"<directory_location>"}
# peference={"download.default_directory" :location}
# options.add_experimental_option("prefs",peference);

# driver = webdriver.Chrome(options=options)
# driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
# driver.maximize_window()


# driver.find_element(By.XPATH,"//button[normalize-space()='Download']").click()
# time.sleep(5)
# driver.close()

#Example 2 Edge Browser
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
#
# #Case 1 (download to the default location)
# driver = webdriver.Edge()
# driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
# driver.maximize_window()
#
# #This code will download the file in default location
# driver.find_element(By.XPATH,"//button[normalize-space()='Download']").click()
# time.sleep(5)
#
# driver.close()

#Case 2 I want to download in the required location
# import os
# location=os.getcwd()
# options=webdriver.EdgeOptions()
# peference={"download.default_directory" :location}
# options.add_experimental_option("prefs",peference)
#
# driver = webdriver.Edge(options=options)
# driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
# driver.maximize_window()
#
# driver.find_element(By.XPATH,"//button[normalize-space()='Download']").click()
# time.sleep(5)
#
# driver.close()

#Example 3 Firefox Browser
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

#Case 1 (download to the default location)
driver = webdriver.Firefox()
driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
driver.maximize_window()

#This code will download the file in default location
driver.find_element(By.XPATH,"//button[normalize-space()='Download']").click()
time.sleep(5)

driver.close()

#Case 2 download in the required location
import os
location=os.getcwd()
options=webdriver.FirefoxOptions()

options.set_preference("browser.download.folderList",0)
options.set_preference("browser.download.manager.showWhenStarting",False)
options.set_preference("browser.download.dir",location)
#Example:profile.set_preference("browser.download.dir","C:\Tutorial\down")
options.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv")

driver = webdriver.Firefox(options=options)
driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[normalize-space()='Download']").click()
time.sleep(5)

driver.close()