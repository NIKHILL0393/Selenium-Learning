import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By


class Booking(webdriver.Chrome):
    def __init__(self,driver_path=r"Desktop:/selenium",teardown=False):
        self.driver_path=driver_path
        self.teardown=teardown
        os.environ['PATH']+=self.driver_path
        super(Booking,self).__init__()
        self.implicitly_wait(20)
        self.maximize_window()  
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def select_place_to_go(self,place_to_go):
        search_field=self.find_element(By.CLASS_NAME,'ce5ee7d913')
        search_field.clear()
        search_field.send_keys(place_to_go)
         
        first_result=self.find_element(By.CSS_SELECTOR,'button[tabindex="-1"]')
        first_result.click()

    def select_dates(self,check_in_date,check_out_date):
        check_in_element=self.find_element(By.CSS_SELECTOR,f'td[data_date="{check_in_date}"]')
        check_in_date.click()           
 
        check_out_element=self.find_element(By.CSS_SELECTOR,f'td[data_date="{check_out_date}"]')
        check_out_date.click()

    def select_adults(self,count):
        selection_element=self.find_element(By.CLASS_NAME,'d7772b248')
        selection_element.click()
     
        while True:
            decrease_adults_element=self.find_element(By.CLASS_NAME,'button[taabindex="-1"]')
            decrease_adults_element.click()

            adults_value_element=self.find_element(By.CLASS_NAME,'d723d73d5f')
            adults_value=adults_value_element.get_attribute('value')
            if int(adults_value)==1:
                break
             
            increase_button_element=self.find_element(By.CLASS_NAME,'eedba9e88a')

            for i  in range(count-1):
                increase_button_element.click() 
        
        def click_search(self):
            search_button=self.find_element(By.CSS_SELECTOR,'buttton[type="submit"]') 
            search_button.click()
        

