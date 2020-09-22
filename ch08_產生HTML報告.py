from HTMLTestRunner import HTMLTestRunner
import unittest
from selenium import webdriver

class Baidu(unittest.TestCase):
     
    def setUp(self):
        self.drive = webdriver.Chrome()
        self.drive.get('http://www.baidu.com/')
        self.drive.implicitly_wait(20)
        
    def baidu_test(self):
        self.drive.find_element_by_id('kw').send_keys('HTMLTestRunner')
        self.drive.find_element_by_id('su').click()
        
    def tearDown(self):
        self.drive.quit()
        
if __name__ == "__main__":
    
    suite = unittest.TestSuite()
    suite.addTest(Baidu('baidu_test'))
    
    fp = open('./result.html','wb')
    runner = HTMLTestRunner(stream = fp,
                            title = "百度搜索報告測試",
                            description = '使用案例狀況')
    runner.run(suite)
    fp.close()