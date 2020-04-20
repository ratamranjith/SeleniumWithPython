import unittest
from dev.Test.TestCase1 import TestCase1_UserName
from dev.Test.TestCase2 import TestCase2_Password

class TestSuite(unittest.TestSuite):
    
    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(TestCase1_UserName('test_WaitForLoginPage'))
        suite.addTest(TestCase2_Password('test_WaitForLoginPage'))
        return suite
    
if __name__ == "__main__":
    unittest.main()