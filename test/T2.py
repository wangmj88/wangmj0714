from selenium import webdriver
import time

ff = webdriver.Firefox()
url = 'https://www.lecuntao.com/shop/index.php?act=login&op=index'
ff.get(url)
ff.find_element_by_id('user_name').send_keys('18500315912')
ff.find_element_by_id('password').send_keys('123456')
time.sleep(10)
ff.find_element_by_id('login_form_submit').click()