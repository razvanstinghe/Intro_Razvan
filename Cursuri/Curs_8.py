from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


webdriver = webdriver.Chrome()
webdriver.get('https://phptravels.net/')  # se apeleaza pagina din browser dupa care se inchide singura
site_rezervari = webdriver.find_element(By.CSS_SELECTOR, 'form[method="GET"] btn-search text-center')
site_rezervari.click()
sleep(50)


# webdriver = webdriver.Chrome()
# webdriver.get('https://www.booking.com')  # se apeleaza pagina din browser dupa care se inchide singura
# site_rezervari = webdriver.find_element(By.CSS_SELECTOR, 'form[method="GET"] button[type="submit"]')
# site_rezervari.click()
# sleep(5000)


# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # Seteaza driverul
# driver = webdriver.Chrome()
#
# # Navigam catre un url
# driver.get('https://phptravels.net/login')
# # Selector by ID
# password_input = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
# login_btn = driver.find_element(By.CSS_SELECTOR, '.btn-box > button[type="submit"]')
#
# password_input.send_keys("ceva")
# login_btn.click()
#
# sleep(50)