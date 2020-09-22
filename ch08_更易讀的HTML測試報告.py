from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
class Baidu(unittest.TestCase):
    
    def setUp(self):
        self.drive = webdriver.Chrome()
        self.drive.implicitly_wait(10)
        self.drive.get('http://www.baidu.com/')
        
    def testBaidu(self):
        self.drive.find_element_by_id('kw').send_keys('selenium')
        self.drive.find_element_by_id('su').click()
        
    def tearDown(self):
        self.drive.quit()
        
if __name__ == '__main__':
    
    Testsuit = unittest.TestSuite()
    Testsuit.addTest(Baidu('testBaidu'))
    
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    file_name = '.' + now + 'result.html'
    fp = open(file_name,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='百度搜索測試報告',
                            description='使用案例執行情況')
    
    runner.run(Testsuit)
    fp.close()
    
    
        