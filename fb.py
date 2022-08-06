import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome("chromedriver.exe")
driver.maximize_window()

driver.get("https://www.facebook.com/login/")
time.sleep(6)
driver.find_element_by_css_selector("#email").send_keys("99898989898") #replace with your facebook phone no or email
time.sleep(5)
driver.find_element_by_css_selector("#pass").send_keys("dontknow@#") #replace with your valid password
time.sleep(5)
driver.find_element_by_css_selector("#loginbutton").click()
time.sleep(30)	
driver.close()		

