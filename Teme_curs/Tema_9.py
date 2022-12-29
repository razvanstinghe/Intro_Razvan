import unittest

import self as self
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from time import sleep
driver = webdriver.Chrome()
class Login(unittest.TestCase):
    def setUp(self):
        base_url = 'https://the-internet.herokuapp.com/'
        self.driver = webdriver.Chrome()
        self.driver.get(base_url)
        self.driver.maximize_window()

        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Form Authentication').click()

    def tearDown(self):

        self.driver.delete_all_cookies()
        self.driver.quit()

    def test_url_corect_Test_1(self):       # este important sa se inceapa def cu "test"
        actual_url = self.driver.current_url
        assert actual_url == 'https://the-internet.herokuapp.com/login', 'You are not on the correct page!'

    def test_page_title_Test_2(self):
        driver.get('https://the-internet.herokuapp.com/login')
        driver.find_element(By.CSS_SELECTOR, 'The internet')

        actual_title = self.driver.title
        assert actual_title == 'The internet'




