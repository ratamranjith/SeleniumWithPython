from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# print(driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div'))

print(driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div'))
driver.quit()