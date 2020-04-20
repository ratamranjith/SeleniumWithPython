from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import unittest

class TestCase1_UserName(unittest.TestCase):
    
    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://facebook.com")        
        
    def test_WaitForLoginPage(self):
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='email']")))
        except: 
            print("Unexpected error:", sys.exc_info()[0])
            
    def tearDown(self):
        driver.quit()
        
if __name__ == "__main__":
    main = unittest.main()