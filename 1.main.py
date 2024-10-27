import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"Desktop:/selenium"
driver = webdriver.Chrome()
driver.get("https://leetcode.com/problemset/")
driver.implicitly_wait(30)
my_element = driver.find_element(By.ID, 'navbar_container')

progress_element=driver.find_element(By.CLASS_NAME,'z-base-2')
print(f"{progress_element.text =='Completed!'}")

WebDriverWait(driver,10).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME,'trustpilot-widget'),#Element filtration
        'Complete!'#expected text
    )
)



