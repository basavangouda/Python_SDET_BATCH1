import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Case==>1
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://www.letskodeit.com/practice")
# driver.maximize_window()
#
# #Find all elements
# hide_button=driver.find_element(By.ID,"hide-textbox")
# hidden_text_field=driver.find_element(By.ID,"displayed-text")
# show_button=driver.find_element(By.ID,"show-textbox")
#
# print(hidden_text_field.is_displayed())
# hidden_text_field.send_keys("QACircle")
# time.sleep(5)
# driver.close()

#Case==>2
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://www.letskodeit.com/practice")
# driver.maximize_window()
#
# #Find all elements
# hide_button=driver.find_element(By.ID,"hide-textbox")
# hidden_text_field=driver.find_element(By.ID,"displayed-text")
# show_button=driver.find_element(By.ID,"show-textbox")
#
# hide_button.click()
# print(hidden_text_field.is_displayed())
# hidden_text_field.send_keys("QACircle")
# time.sleep(5)
# driver.close()

#Case 3 Handling  ElementNotInteractableException
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

#Find all elements
hide_button=driver.find_element(By.ID,"hide-textbox")
hidden_text_field=driver.find_element(By.ID,"displayed-text")
show_button=driver.find_element(By.ID,"show-textbox")

hide_button.click()
print(hidden_text_field.is_displayed())
time.sleep(5)

#Now make disabled element as visible to selenium
driver.execute_script("arguments[0].setAttribute('style','visibility:visible;');",hidden_text_field)
time.sleep(5)
driver.execute_script("document.getElementById('displayed-text').value='Hello Good Morning';")
time.sleep(5)
show_button.click()
time.sleep(5)
driver.close()