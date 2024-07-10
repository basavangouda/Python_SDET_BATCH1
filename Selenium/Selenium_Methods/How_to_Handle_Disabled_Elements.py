from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Case 1
# driver=webdriver.Chrome()
# driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
# time.sleep(5)
# driver.maximize_window()
#
# driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@src='menu.html']"))
#
# # Element 1
# if driver.find_element(By.ID,"ui-id-1").is_enabled():
#     print("Element is enabled state")
# else:
#     print("Element is disabled state")
#
# print(driver.find_element(By.ID,"ui-id-1").text)
#
# print(driver.find_element(By.ID,"ui-id-1").is_displayed())
#
# driver.switch_to.parent_frame()
#
# # Element 2
# if driver.find_element(By.XPATH,"//input[@value='Project-QACircle']").is_enabled():
#     print("Element is enabled state")
# else:
#     print("Element is disabled state")
#
# print(driver.find_element(By.XPATH,"//input[@value='Project-QACircle']").text)
#
# print(driver.find_element(By.XPATH,"//input[@value='Project-QACircle']").is_displayed())
#
# driver.close()

#Case 2
driver=webdriver.Chrome()
driver.get("D:\\Python_SDET_March-2024-Batch\\HTML\\Handling_disabled_Elements.html")
time.sleep(5)
driver.maximize_window()

# Element 1
if driver.find_element(By.ID,"fname").is_enabled():
    print("Element is enabled state")
else:
    print("Element is disabled state")

print(driver.find_element(By.ID,"fname").text)

print(driver.find_element(By.ID,"fname").is_displayed())


# Element 2
if driver.find_element(By.NAME,"birthday").is_enabled():
    print("Element is enabled state")
else:
    print("Element is disabled state")

print(driver.find_element(By.NAME,"birthday").text)

print(driver.find_element(By.NAME,"birthday").is_displayed())

driver.close()
