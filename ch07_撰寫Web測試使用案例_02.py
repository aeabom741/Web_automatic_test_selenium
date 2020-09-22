from selenium import webdriver
import unittest
import time

class Mytest(unittest.TestCase):
    
    def setUp(self):
        self.drive = webdriver.Chrome()
        self.drive.get('http://www.youdao.com/')
        self.drive.implicitly_wait(10)
        
    def test_yudao(self):
        self.drive.find_element_by_name('q').send_keys('webdrive')
        self.drive.find_element_by_name('q').submit()
        time.sleep(3)
        self.assertEqual(self.drive.title,'webdrive - 有道搜索')
        
    def tearDown(self):
        self.drive.quit()
        
if __name__ == "__main__":
    unittest.main()