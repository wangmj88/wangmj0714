from selenium import webdriver
from selenium.webdriver.support.ui import Select
from  wangmj import Login
import time


class test_Login():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.url = "https://www.lecuntao.com/shop/index.php?act=login&op=index"
        self.driver.get(self.url)
        self.driver.implicitly_wait(100)


    def test_order(self):
        Login(self.driver).login("18500315912", "123456")
        time.sleep(3)
        self.driver.get("http://www.lecuntao.com/index.php?act=buyer_index&op=index&")
        time.sleep(3)

