import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Selenium.Utilities import XLUtil
file='D:\\Python_SDET_March-2024-Batch\\Selenium\\Utilities\\Calculate.xlsx'

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
driver=webdriver.Chrome(options=ops)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
time.sleep(5)

rows=XLUtil.getRowCount(file,'Sheet1')
print(rows)

column=XLUtil.getColumnCount(file,'Sheet1')
print(column)

#Read Excel sheet:
for r in range(2,rows+1):
    principle=XLUtil.readData(file,"Sheet1",r,1)
    rate_of_interest=XLUtil.readData(file,"Sheet1",r,2)
    period_ele=XLUtil.readData(file,"Sheet1",r,3)
    type_of_period_ele=XLUtil.readData(file,"Sheet1",r,4)
    frequency_ele=XLUtil.readData(file,"Sheet1",r,5)
    Exp_maturity_value=XLUtil.readData(file,"Sheet1",r,6)

    driver.find_element(By.ID, "principal").send_keys(principle)
    driver.find_element(By.ID, "interest").send_keys(rate_of_interest)
    driver.find_element(By.ID, "tenure").send_keys(period_ele)
    drop_down1=Select(driver.find_element(By.NAME,"tenurePeriod"))
    drop_down1.select_by_visible_text(type_of_period_ele)

    drop_down2=Select(driver.find_element(By.ID,"frequency"))
    drop_down2.select_by_visible_text(frequency_ele)

    #Click on calculate button
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()
    time.sleep(5)

    Act_maturity_value = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

    if float(Exp_maturity_value)==float(Act_maturity_value):
        print("Test Pass")
        XLUtil.WriteData(file,"Sheet1",r,8,"Passed")
        XLUtil.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("Test Fail")
        XLUtil.WriteData(file, "Sheet1", r, 8, "Failed")
        XLUtil.fillRedColor(file, "Sheet1", r, 8)

    #CLick on Clear button
    driver.find_element(By.XPATH, "//div[@class='CTR PT15']/a[2]/img").click()

driver.close()


