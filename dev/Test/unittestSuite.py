from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import unittest

class WaitForElements(unittest.TestCase):
    
    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.facebook.com")
        
        
    def test_WaitForLoginPage(self):
        try:
            bLocator = '//*[@id="blueBarDOMInspector"]/div/div/div/div[1]/h1/a/i'
            logoImage = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(By.XPATH, bLocator))
        except: 
            print("Exception thrown")
            
    def tearDown(self):
        driver.quit()
        
if __name__ == "__main__":
    unittest.main()