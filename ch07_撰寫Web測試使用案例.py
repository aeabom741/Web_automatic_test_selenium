from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class MyTest(unittest.TestCase):
    
    def setUp(self):
        self.drive = webdriver.Chrome()
        self.drive.get('http://www.baidu.com/')
        self.drive.implicitly_wait(30)
    
    def test_baidu(self):
        self.drive.find_element_by_id('kw').clear()
        self.drive.find_element_by_id('kw').send_keys('unittest')
        self.drive.find_element_by_id('su').click()
        time.sleep(3)
        title = self.drive.title
        self.assertEqual(title,'unittest_百度搜索')
    def tearDown(self):
        self.drive.quit()
        
if __name__ == "__main__":
    unittest.main()