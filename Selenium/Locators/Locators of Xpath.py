#XML path language ===> Xpath
#This Xpath is used to locate the element uniquely in the DOM tree

"""
Basic Syntax
//tag_name[@attribute='Value']

//==> stands for current node

tag_name ==> It might be input,div,span etc.
@attribute ==> Name of attribute can be class, id,aria-label etc.
'Value' ==> Value of the respective attribute.

"""

#Types of Xpath
"""
Xpath has been divided into two types 
Absolute Xpath : Full Xpath 
        /html/body/div[3]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[2]
        /html/body/form/input[3]
        
Relative Xpath : 
        //div[text()='Cart']
        //input[@name='email']

"""
#Sample Selenium script with absolute and Relative Xpath
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
#
# #Absolute Xpath
# driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/input").click()
# time.sleep(5)
#
# #Relative Xpath
# driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Hello Good Morning")
# time.sleep(5)
#
# driver.close()


"""
ID ==> //*[@id='some name']

Class ==> //*[@class='Value of the class']

Img ==> //img[@src='https://images.mamaearth.in/svg/user-header-white.svg']

"""
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.linkedin.com/")
driver.maximize_window()

#Relative Xpath
#Email id text field
driver.find_element(By.XPATH,"//*[@id='session_key']").send_keys("Hello Good Morning")
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='session_key']").clear()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@name='session_key']").send_keys("Hello Good Morning")
time.sleep(5)

#password Text field
driver.find_element(By.XPATH,"//input[@name='session_password']").send_keys("Hello")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@name='session_password']").clear()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='session_password']").send_keys("Good Morning")
time.sleep(5)

driver.close()
"""
#To get the list of images on the web pages
#XPath == //img

#To get the list of links present on the web page
#Xpath =//a

#What is the difference between single slash and double slash in selenium
# single forward slash (/) selects only the immediate child elements,
# while the double forward slash (//) selects all descendants of the current node,
# regardless of their level.

#Xapth with COntains() function
"""
contains()
#With full attribute Value
//html_tag name[contains(@attribute,'attribute value')]

#With Partial attribute Value
//html_tag name[contains(@attribute,'Partial value')]
"""

#Example 1
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://www.nykaa.com/")
# driver.maximize_window()
# time.sleep(5)
#Sign in button
# driver.find_element(By.XPATH,"//button[contains(@class,'css-1gzc5zn')]").click()
# time.sleep(5)

#Sign in button
# driver.find_element(By.XPATH,"//button[contains(@kind,'primary')]").click()
# time.sleep(5)

#Sign in button
# driver.find_element(By.XPATH,"//button[contains(@aria-label,'Kebab menu')]").click()
# time.sleep(5)

#Category
# driver.find_element(By.XPATH,"//a[contains(@id,'category')]").click()
# time.sleep(5)
# driver.close()

#Example Usage of contains() for xpath in selenium
"""
Name Attribute
        //tag_name[contains(@name,'attribute Value')]

Xpath contains function for Href attribute
        //tag_name[contains(@href,'some/link')]

        //a[contains(@href,"/installApp")]

Xpath contains function for img with src attribute
        //img[contains(@src,"some/path/link.png")]

        //img[contains(@src,'https://images-static.naikaa.com/media/wysiwyg/uiTools/2023-10/Lakme_118x55pxls.png')]

Xpath contains function for type  attribute

         //tag_name[contains(@type,'attribute Value')]
"""

#Xapth Matching the text elements : text() => extact text or Partial text
#tag_name[text()='text_value']

#Example 1
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://www.firstcry.com/")
# driver.maximize_window()
# time.sleep(5)
# x=driver.find_element(By.XPATH,"//span[text()='Track Order']")
# print(x.text)
# if "TrackOrder"==x.text:
#     x.click()
# time.sleep(5)
#
# z=driver.find_element(By.XPATH,"//span[text()='FirstCry Parenting']")
# print(z.text)
# # if "FirstCry Parenting"==z.text:
# #     z.click()
# #     assert "Baby Products Online India: Newborn Baby Products & Kids Online Shopping at FirstCry.com"==driver.title
# #     print("Test Pass")
#
# time.sleep(5)
# y=driver.find_element(By.XPATH,"//span[contains(text(),'Reg')]").text
# print(y)
# time.sleep(5)
# driver.close()


# Using Conditions ( OR /AND )
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
# time.sleep(5)
# driver.find_element(By.XPATH,"//input[@id='user-name' or @class='input_error form_input']").send_keys("Hello Good Morning")
# time.sleep(5)
# driver.find_element(By.XPATH,"//input[@id='password'  and @class='input_error form_input' ]").send_keys("QACircle")
# time.sleep(5)
# driver.find_element(By.ID,"login-button").click()
# time.sleep(5)
# driver.close()

#Starts-with Xpath :
"""
Syntax : //tagName[starts-with(@attribute,'starting-value')]
         //input[starts-with(@id,'searchbox')]

Note : ends-with xpath in selenium not working
The issue is: starts-with is available in XPath 1.0 while ends-with was only 
introduced by XPath 2.0 . Selenium supports XPath 1.0 only. 
That's why ends-with will not work with Selenium. 
But you still can use contains with Selenium

Ends with will not work with xapth 1.0 Version and selenium will not support
: //tagName[ends-with(@attribute,'starting-value')]
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
# time.sleep(5)
# driver.find_element(By.XPATH,"//input[starts-with(@class,'submit-button')]").click()
# time.sleep(5)
# driver.close()

#Xpath with Normalize Space :
"""
Syntax : normalize-space([string])

#Using Contains Function
Scenario 1:  //div[contains(text(),'space in beginning and end')] (Pass) 

Scenario 2 : //div[contains(text(),'space in between')] (Fail)

Scenario 3 : //div[contains(text(),auto pract')] (Fail)
             
Scenario 4 :  //div[contains(text(),'programs buzz')] (Fail)

Scenario 5 : Attribute with space in the beginning and end
            //div[contains(@class,'my class 1')] ===(Pass) 

Scenario 6 : Attribute with space in between
            //div[contains(@class,'my class 2')] ===(Fail)

Normalize-space with text() function: 
Scenario 1: Text with space in the beginning and end
            //div[text()[normalize-space()= 'space in beginning and end']] ==>Pass
            //div[normalize-space(text())= 'space in beginning and end'] ==>Pass

Scenario 2: Text with space in between
            //div[text()[normalize-space()='space in between']] ==>Pass
            //div[normalize-space(text())='space in between'] ==>Pass

Scenario 3: Text with nested elements with inner text
            //div[text()[normalize-space()='auto']]  ==>Pass
            //div[text()[normalize-space()='buzz']]   ==>Pass

Scenario 4: Text with nested elements with inner text 
            //div[text()[normalize-space()='auto pract']] ====> Fail
            //div[text()[normalize-space()='programs buzz']] ====> Fail

Normalize space with contains() function
Scenario 1: Text with space in the beginning and end
            //div[contains(normalize-space(),'space in beginning and end')] ==> Its not finding unique element , instead finding 2 elements
            
Scenario 2: Text with space in between
            //div[contains(normalize-space(),'space in between')]
            
Scenario 3: Text with nested elements with inner text
"""
#Xpath Axes :
"""
1. Self  
2. Child 
3. Parent 
4. Following
5. Preceding 
6. Following Sibling
7. Preceding Sibling 
8. Ancestor
9.Descendant 

1. Self : Self node means whichever node we start
    Syntax ==> //*[@attribute='value']/self::tagname
    
    //*[@type='submit']/self::input

2. Child : Child axes are used to traverse all the child elements of the current html tag
    Syntax ==> //*//*[@attribute='value']/child::child tagname
    
    //div[@id="reg_form_box"]/child::div[11]/button

"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver=webdriver.Chrome()
# driver.get("https://www.facebook.com/r.php")
# driver.maximize_window()
# time.sleep(5)
# element=driver.find_element(By.XPATH,"//div[@id='reg_form_box']/child::div[11]/button")
# print(element.text)
# time.sleep(5)
# element.click()
# print("Element is clicked successfully")
# time.sleep(5)
# driver.close()

"""
3. Parent  : Parent axes are used to traverse parent elements of the current html tag
    Syntax ===> //*[@attribute='value']/parent::parent tag name
    
    //div[@class='FPdoLc lJ9FBc']//input[@class='gNO89b']/parent::*/parent::*/parent::*/div[1]
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver=webdriver.Chrome()
# driver.get("https://www.google.com/")
# driver.maximize_window()
# time.sleep(5)
# element=driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']//input[@class='gNO89b']/parent::*/parent::*/parent::*/div[1]")
# element.click()
# time.sleep(5)
# driver.find_element(By.NAME,"q").send_keys("QACircle")
# print("Test Pass")
# time.sleep(5)
# driver.find_element(By.XPATH,"//div[@class='lJ9FBc']//input[@class='gNO89b']").click()
# time.sleep(5)
# driver.close()

"""
4. Following
Following Xpath axes are used to traverse all elements that come after the current html tag
//Tag Name[@attribute='Value']/following::tagname

//input[@placeholder='Search Amazon.in']/following::a[contains(text(),'Best Sellers')][1] 

"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver=webdriver.Chrome()
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# element=driver.find_element(By.XPATH,"//input[@placeholder='Search Amazon.in']/following::a[contains(text(),'Best Sellers')][1]")
# print(element.text)
# time.sleep(5)
# element.click()
# time.sleep(5)
# driver.close()

"""
5. Preceding
Preeceding Xpath axes are used to traverse all nodes that come before current html tag

//Tag Name[@attribute='Value']/preceding::tagname

Element 1 = //input[@id='twotabsearchtextbox']/preceding::span[3]
Element 2 = //input[@id='twotabsearchtextbox']/preceding::span[contains(text(),'Update location')]

"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver=webdriver.Chrome()
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# element=driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']/preceding::span[contains(text(),'Update location')]")
# print(element.text)
# time.sleep(5)
# element.click()
# time.sleep(5)
# driver.close()

"""
6. Following Sibling

Syntax ==> current html tag[@attribute='value']/following-sibling::sibling tag[@attribute='Value']

Element = //a[contains(text(),'Best Sellers')]/following-sibling::a[1]
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver=webdriver.Chrome()
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# element=driver.find_element(By.XPATH,"//a[contains(text(),'Best Sellers')]/following-sibling::a[1]")
# print(element.text)
# time.sleep(5)
# element.click()
# time.sleep(5)
# driver.close()


"""
7. Preceding Sibling 

Syntax ==> current html tag[@attribute='value']/preceding-sibling::sibling tag[@attribute='Value']

Element == //a[contains(text(),'Best Sellers')]//preceding-sibling::a[3]
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver=webdriver.Chrome()
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# element=driver.find_element(By.XPATH,"//a[contains(text(),'Best Sellers')]//preceding-sibling::a[text()='Sell']")
# print(element.text)
# time.sleep(5)
# element.click()
# time.sleep(5)
# driver.close()

"""
8. Ancestor ==>https://www.facebook.com/r.php

//*[attribute='value']/ancestor::tag name

//*[contains(text(),'Female')]/ancestor::div[2]//input[@name='reg_email__']
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.facebook.com/r.php")
# time.sleep(5)
# e=driver.find_element(By.XPATH,"//*[contains(text(),'Female')]/ancestor::div[2]//input[@name='lastname']")
# print(e.text)
# print("Ancestor element is identified")
# e.send_keys("Hello")
# time.sleep(5)
# driver.close()
"""
9.Descendant 

Syntax ==> //tag Name[attribute='Value']/descendant::tag Name

Xpath ==> //div[@id='nav-xshop-container']/descendant::a[10]
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/")
time.sleep(5)
e=driver.find_element(By.XPATH,"//div[@id='nav-xshop-container']/descendant::a[10]")
print(e.text)
print("Descendant element is identified")
e.click()
time.sleep(5)
driver.close()