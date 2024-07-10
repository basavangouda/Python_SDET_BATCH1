from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://www.firstcry.com/")
driver.maximize_window()
time.sleep(5)
search_box=driver.find_element(By.ID,"search_box")
search_box.clear()

search_box.send_keys("baby")
driver.implicitly_wait(10)

auto_sugg=driver.find_elements(By.XPATH,"//li[@class='txtcl autoseg match']/span[1]")
print(len(auto_sugg))
l1=[]
for single_sugg in auto_sugg:
    print(single_sugg.text)
    l1.append(single_sugg.text)

print(l1)
for single_sugg in auto_sugg:
    if single_sugg.text=="Baby masks":
        single_sugg.click()
        break

time.sleep(5)
driver.close()