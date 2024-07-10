# CSS => Cascading Style sheet
#CSS Selector faster than the Xpath

# Case 1 ==> Simple
""" ID

Xpath ==> "[@id='example']
CSS ==> #example

"""
#Example 1
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
# time.sleep(5)
#Username Text field
# driver.find_element(By.CSS_SELECTOR,"input#user-name").send_keys("QACircle")
# time.sleep(5)
# driver.close()

#Example 2
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://app.hubspot.com/login")
# driver.maximize_window()
# time.sleep(5)
#Email id text field
# driver.find_element(By.CSS_SELECTOR,"input#username").send_keys("Hello Good Morning")
# time.sleep(5)
# driver.close()



""" Element finding PARENT TO CHILD 

Synatx : Parent Tag > Child Tage
Xpath : //div/input

Css  : div >input

****** For Finding Sub child *****
Xpath ==> //div//input

Css ==> div input 

"""
#Parent >  child
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://app.hubspot.com/login")
# driver.maximize_window()
# time.sleep(5)
##Email id text field
# driver.find_element(By.CSS_SELECTOR,"div >input#username").send_keys("Hello Good Night")
# time.sleep(5)
# driver.close()


#Parent  Child
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://app.hubspot.com/login")
# driver.maximize_window()
# time.sleep(5)
# #Email id text field
# driver.find_element(By.CSS_SELECTOR,"div  input#username").send_keys("Hello Tata bye bye")
# time.sleep(5)
# driver.close()

#Class
"""" 
Xpath ==> [@class='example']
CSS ==> .example 

htmltagename.c1.c2.c3

"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
# time.sleep(5)
# # Text field
# #driver.find_element(By.CSS_SELECTOR,"input.input_error").send_keys("QACircle")
# driver.find_element(By.CSS_SELECTOR,"input.input_error.form_input").send_keys("QACircle")
# time.sleep(5)
# driver.close()

#I want combine ID and Class name while finding an element using CSS
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://app.hubspot.com/login")
# driver.maximize_window()
# time.sleep(5)
# # Text field
# #driver.find_element(By.CSS_SELECTOR,"input.input_error").send_keys("QACircle")
# driver.find_element(By.CSS_SELECTOR,"#password.form-control.private-form__control.login-password.m-bottom-3").send_keys("QACircle")
# time.sleep(5)
# driver.close()

#Same Above code we can write half class name to find element using CSS

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://app.hubspot.com/login")
# driver.maximize_window()
# time.sleep(5)
# # Text field
# #driver.find_element(By.CSS_SELECTOR,"input.input_error").send_keys("QACircle")
# driver.find_element(By.CSS_SELECTOR,".login-password.m-bottom-3").send_keys("QACircle123")
# time.sleep(5)
# driver.close()

#Case 2 - Advanced

#1 Attribute Values
"""
Xpath ==> //input [@name='username']
Css ==>input[name='username']

We can combine 2 attributes to be more specific

Css ==> input[name='login'][type='submit]

"""

#Find element using Single Attribute :
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
# time.sleep(5)
# # Username Text field
# driver.find_element(By.CSS_SELECTOR,"input[name='user-name']").send_keys("Python SDET")
# time.sleep(5)
# driver.close()

#Find element using Two Attribute :
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
# time.sleep(5)
# # Username Text field
# driver.find_element(By.CSS_SELECTOR,"input[class='input_error form_input'][placeholder='Password']").send_keys("Python SDET")
# time.sleep(5)
# driver.close()

#2  Using Nth-child

#Next sibling using Nth of Type
# #Example 1
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("file:///D:/QACircle%20Details/Python%20SDET/Selenium%20-Python/CSS_Selector_NextSimbling%20and%20Nth%20Type.html.html")
# driver.maximize_window()
# time.sleep(5)
# # Find Car element from the HTML tree and navigate to Goat
# x=driver.find_element(By.CSS_SELECTOR,"#recordlist li:nth-of-type(3)+li")
# print(x.text)
# time.sleep(5)
# driver.close()

#Example 2
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://mamaearth.in/")
# driver.maximize_window()
# time.sleep(5)
# # Find Car element from the HTML tree and navigate to Goat
# x=driver.find_element(By.CSS_SELECTOR,".mainMenu li:nth-of-type(1)+li")
# print(x.text)
# time.sleep(5)
# driver.close()

"""
Note : If we don't specify the child type for nth-child it will allow you to select the
particular child element with specifed number(Fourth Child) without regards of Type.
This may be useful in testing css layout in selenium

Css===> #recordlist *:nth-child(4)

"""

# #Example 1
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("file:///D:/QACircle%20Details/Python%20SDET/Selenium%20-Python/CSS_Selector_NextSimbling%20and%20Nth%20Type.html.html")
# driver.maximize_window()
# time.sleep(5)
# # Find Car element from the HTML tree and navigate to Goat
# x=driver.find_element(By.CSS_SELECTOR,"#recordlist *:nth-child(3)")
# print(x.text)
# time.sleep(5)
# driver.close()

#Example 2
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://mamaearth.in/")
# driver.maximize_window()
# time.sleep(5)
# # Find Car element from the HTML tree and navigate to Goat
# x=driver.find_element(By.CSS_SELECTOR,".mainMenu *:nth-child(1)")
# print(x.text)
# time.sleep(5)
# driver.close()

#3 Selecting the first child
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://signup.pcloudyunified.com/")
# driver.maximize_window()
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"div[class='iti__selected-flag'][aria-controls='iti-0__country-listbox']").click()
# time.sleep(5)
# print(driver.find_element(By.CSS_SELECTOR,"#iti-0__country-listbox >li:first-child").text)
# time.sleep(5)
# driver.close()

#4 Selecting the last child
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://signup.pcloudyunified.com/")
# driver.maximize_window()
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"div[class='iti__selected-flag'][aria-controls='iti-0__country-listbox']").click()
# time.sleep(5)
# print(driver.find_element(By.CSS_SELECTOR,"#iti-0__country-listbox >li:last-child").text)
# time.sleep(5)
# driver.close()

#Using Substring :
#Prefix ==>starting with
#Suffix ==> ending with
#substring (contains) ==> To handle dynamic elements
#Matching with word

#Prefix ==>starting with
"""
<HTML Tag><[attribute^='prefix of the string']>
input[name^='pass']

"""
#Example 1:
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://signup.pcloudyunified.com/")
# driver.maximize_window()
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"input[id^='txtuserF']").send_keys("Hello Good Morning")
# time.sleep(5)
# driver.close()

#Example 2:
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
# time.sleep(5)
# x=driver.find_element(By.CSS_SELECTOR,"input[class^='submit-butt']")
# print(x.text)
# print("Hello")
# driver.find_element(By.CSS_SELECTOR,"input[class^='submit-butt']").click()
# time.sleep(5)
# driver.close()

#Example 3:
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://mamaearth.in/")
# driver.maximize_window()
# time.sleep(5)
# x=driver.find_element(By.CSS_SELECTOR,"div[class^='icon-la']")
# print(x.text)
# print("Hello")
# time.sleep(5)
# driver.close()


#Suffix ==> ending with
"""
Syntax : <HTML Tag><[attribute$='suffix of the string']>
         input[name$='rd']
"""
#Example 1:
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://signup.pcloudyunified.com/")
# driver.maximize_window()
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"input[id$='Id']").send_keys("Hello Good Morning tata bye bye")
# time.sleep(5)
# driver.close()

#Example 2:
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"input[placeholder$='name']").send_keys("Hello Tata Bye Bye")
# time.sleep(5)
# driver.close()

#Example 3:
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://mamaearth.in/")
# driver.maximize_window()
# time.sleep(5)
# #Search button
# driver.find_element(By.CSS_SELECTOR,"button[class$='-button']").click()
# time.sleep(5)
#driver.close()


#substring (contains) ==> To handle dynamic elements
"""
Syntax : <HTML Tag><[attribute *='sub string']>
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://signup.pcloudyunified.com/")
# driver.maximize_window()
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"input[id*='ull']").send_keys("QACircle Software Training Academy")
# time.sleep(5)
# driver.close()

#Matching with word
"""
Syntax : <HTML Tag><[attribute ~='sub string']>
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://mamaearth.in/")
driver.maximize_window()
time.sleep(5)
y=driver.find_elements(By.CSS_SELECTOR,"li[class~='category']")
for x in y:
    print(x.text)
time.sleep(5)
driver.close()
