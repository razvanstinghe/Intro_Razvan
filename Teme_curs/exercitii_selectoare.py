from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# Seteaza driverul
driver = webdriver.Chrome()


# Navigam catre un url
driver.get('https://phptravels.net/login')
# # Selector by CLASS NAME
driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys('cevaaaaaaa')
# password_input.send_keys('cevaaaaaaa')
# first_name.send_keys('Andy')
sleep(10)

# Selector by ID
# driver.get('https://phptravels.net/')
# element_ID = driver.find_element(By.CSS_SELECTOR, 'class="flight_type form-select form-select-sm"')
# # password_input.send_keys('cevaaaaaaa')
# # first_name.send_keys('Andy')
# sleep(500)


# driver.get('https://phptravels.net/')
# # Selector by Class - ia primul tot timpul - este ok sa il folosim doar daca avem clasa unica
# driver.find_element(By.CLASS_NAME, 'form-select-sm').send_keys('Business')
# sleep(500)

# # # Selector by Name
# driver.get('https://phptravels.net/')
# driver.find_element(By.NAME, 'country').send_keys('Romania')