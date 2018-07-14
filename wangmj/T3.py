from selenium import webdriver
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
ff = webdriver.Firefox()
url = 'https://www.lecuntao.com/shop/index.php?act=login&op=index'
ff.get(url)
time.sleep(5)
ff.find_element_by_id('user_name').send_keys('18500315912')
ff.find_element_by_id('password').send_keys('123456')
time.sleep(10)
ff.find_element_by_id('login_form_submit').click()
time.sleep(3)
ff.get('http://www.lecuntao.com/shop/item-565686.html')