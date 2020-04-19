from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.oselabs.com/contact-us")
driver.close()