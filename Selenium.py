# from selenium import webdriver
#
# # System.setProperty("webdriver.gecko.driver","path of geckodriver.exe");
# # WebDriver driver = new FirefoxDriver();
#
# from selenium.webdriver.firefox.options import Options
# options = Options()
# options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
# driver = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)
# driver.get('http://google.com/')
#
# # driver = webdriver.Chrome(executable_path="C:\Webdrivers\chromedriver.exe")
# #
# # driver.get("https://www.youtube.com")

class Romania():
    def language(self):
        print("Romanian")


class USA():
    def language(self):
        print("English")

obj_ro = Romania()
obj_en = USA()
for country in (obj_ro, obj_en):
    country.language()

limba_1 = Romania()
limba_2 = USA()

# def add(x, y, z=0):
#     return x + y + z
#
# print(add(2, 3, 8))