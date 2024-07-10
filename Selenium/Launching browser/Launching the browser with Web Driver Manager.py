#Chrome
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(5)
driver.get("https://mamaearth.in/")
driver.maximize_window()
time.sleep(5)
Exp_Result="Mamaearth Summer Sale is Live! Buy 3 Pay For 2"
Act_Result=driver.title
print(Act_Result)
if Act_Result==Exp_Result:
    print("Test Pass")
else:
    print("Test Fail")
driver.close()

#Mozilla FireFox
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

#from selenium.webdriver.firefox.options import Options
#option=Options()
#option.binary_location="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
#service_obj=Service("C:\\Driver\\geckodriver.exe")
#driver=webdriver.Firefox(service=service_obj,options=option)

driver=webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
time.sleep(5)
driver.get("https://mamaearth.in/")
driver.maximize_window()
Exp_Result="Mamaearth Summer Sale is Live! Buy 3 Pay For 2"
Act_Result=driver.title

if Act_Result==Exp_Result:
    print("Test Pass")
else:
    print("Test Fail")
driver.close()

#Edge
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as edgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#service_obj=Service("C:\\Driver\\msedgedriver.exe")
#driver=webdriver.Edge(service=service_obj)

driver=webdriver.Edge(service=edgeService(EdgeChromiumDriverManager().install()))
driver.get("https://mamaearth.in/")
driver.maximize_window()
Exp_Result="Mamaearth Summer Sale is Live! Buy 3 Pay For 2"
Act_Result=driver.title

if Act_Result==Exp_Result:
    print("Test Pass")
else:
    print("Test Fail")
driver.close()