import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r"Desktop:/selenium"
driver = webdriver.Chrome()

driver.get('https://www.w3schools.com')

driver.implicitly_wait(10)
search2 = driver.find_element(By.ID,'search2')

#sending keys
search2.send_keys('HTML')
#search2.send_keys(Keys.NUMPAD1,Keys.NUMPAD4)

#CSS Selector
btn=driver.find_element(By.CSS_SELECTOR,'button[onclick="click_learntcode_search_btn()"]')
btn.click()
 