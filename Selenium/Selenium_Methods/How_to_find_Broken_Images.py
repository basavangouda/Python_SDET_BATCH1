import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

#https://www.nykaa.com/
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://hubspot.com/")
driver.maximize_window()

#Find all image elements
images=driver.find_elements(By.XPATH,"//img")
print(len(images))

#Check each image
broken_image=[]
for image in images:
    src=image.get_attribute("src")
    try:
        response=requests.get(src,timeout=5)
        if response.status_code!=200:
            broken_image.append(src)
    except requests.exceptions.RequestException as e:
        broken_image.append(src)
        print("Error with image", src,":",e)

#Report the brokwn images
if broken_image:
    print('Found the broken images',len(broken_image))
    for img in broken_image:
        print(img)
else:
    print("No Broken images found")

driver.close()



