from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# Seteaza driverul
driver = webdriver.Chrome()


# Navigam catre un url
# driver.get('https://phptravels.net/login')
# # # Selector by CLASS NAME
# driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys('cevaaaaaaa')
# # password_input.send_keys('cevaaaaaaa')
# # first_name.send_keys('Andy')
# sleep(10)

# Selector by ID
# driver.get('https://phptravels.net/')
# element_ID = driver.find_element(By.CSS_SELECTOR, 'class="flight_type form-select form-select-sm"')
# password_input.send_keys('cevaaaaaaa')
# first_name.send_keys('Andy')
# sleep(500)


# driver.get('https://phptravels.net/')
# # Selector by Class - ia primul tot timpul - este ok sa il folosim doar daca avem clasa unica
# driver.find_element(By.CLASS_NAME, 'form-select-sm').send_keys('Business')
# sleep(500)

 # Selector by Name & class name

# driver.get('https://www.seleniumframework.com/Practiceform/')
# driver.find_element(By.NAME, 'country').send_keys('Romania')
# driver.find_element(By.NAME, 'message').send_keys('e grea testarea automata')
# driver.find_element(By.NAME, 'telephone').send_keys('0722938910')
# driver.find_element(By.CLASS_NAME, 'dt-btn-submit').click()

# driver.get('https://google.com')
# driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
# driver.find_element(By.CSS_SELECTOR, 'input.gLFyf').send_keys('dy')
# driver.get('')
# driver.find_element(By.XPATH, '//span[text()="Creează un cont"')       # nu merge
# sleep(20)

# get_title = driver.title
# driver.get("https://www.google.com/")
# # print(get_title, " ", len(get_title))
# driver.find_element(By.CLASS_NAME, 'Gdd5U').click()
# driver.find_element(By.CSS_SELECTOR, 'input[title="Caută"]').send_keys('dcahcdhac')

driver.get("https://phptravels.net/timeout")
driver.find_element(By.LINK_TEXT, 'Back to Homepage').click()          # OK
driver.find_element(By.CLASS_NAME, 'featured_flight_12').click()       # nu merge

sleep(20)