from pycparser.c_ast import ID
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Seteaza driverul
driver = webdriver.Chrome()

# -----------------SELECTOR: ID----------------
# driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
# driver.find_element(By.ID,'datepicker').send_keys('15.12.2022')     # OK
# driver.find_element(By.ID, "sex-0").click()                         # OK
# driver.find_element(By.ID, "profession-1").click()                  # OK
#
# sleep(200)

# -----------------SELECTOR: LINK TEXT----------------
# # Navigam catre un url
# driver.get('https://www.techlistic.com/p/java.html')
# # # Selector by Link Text
# driver.find_element(By.LINK_TEXT, 'href="https://www.techlistic.com/p/java.html"').click()
# driver.find_element(By.LINK_TEXT, 'Autocomplete').click()
#
# sleep(20)

# -----------------SELECTOR: PARTIAL LINK TEXT----------------
# # Selector by Partial Link Text
# driver.get('https://www.techlistic.com/p/selenium-practice-form.html')

# sleep(15)

# -----------------SELECTOR: NAME----------------
# driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
#
# driver.find_element(By.NAME, 'firstname').click()                   # OK
# driver.find_element(By.NAME, 'firstname').send_keys('Razvan')       # OK
# #
# driver.find_element(By.NAME, 'lastname').click()                    # OK
# driver.find_element(By.NAME, 'lastname').send_keys('Stinghe')       # OK
#
# sleep(20)

# -----------------SELECTOR: TAG----------------

driver.get('https://phptravels.net/hotels')
driver.find_element(By.TAG_NAME, '').click()
sleep(20)
# -----------------SELECTOR: CLASS----------------
# driver.get('https://phptravels.net/')

# driver.find_element(By.CLASS_NAME, 'dropdown-btn').click()                      # OK
# driver.find_element(By.CLASS_NAME, 'btn-primary').click()                       # OK
# driver.get('https://phptravels.net/flights')
# flight_class = driver.find_element(By.CLASS_NAME, 'form-select-sm').send_keys('Business')   # OK
#
# sleep(15)
