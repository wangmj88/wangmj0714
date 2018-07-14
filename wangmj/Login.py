from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
class Login():
        def __init__(self,driver):
                self.driver = driver

        def login(self,username,password):
            self.driver.find_element_by_id('user_name').send_keys('username')
            self.driver.find_element_by_id('password').send_keys('password')
            time.sleep(10)
            self.driver.find_element_by_id('login_form_submit').click()




