from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.drive = webdriver.Chrome()
        self.drive.implicitly_wait(30)
        self.drive_url = 'http://www.baidu.com/'
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def Test_baidu(self):
        drive = self.drive
        drive.get(self.drive_url)
        drive.find_element_by_id('kw').clear()
        drive.find_element_by_id('kw').send_keys('selenium ide')
        drive.find_element_by_id('su').click()
        
    def is_element_present(self, how, what):
        try:
            self.drive.find_element(by = how, value = what)
        except NoSuchElementException as e:
            print(e)
        return True
    
    def is_alert_present(self):
        try:
            self.drive.switch_to_alert()
        except NoAlertPresentException as e:
            print(e)
        return True
    
    def close_alert_and_get_it_text(self):
        try:
            alert = self.drive.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True
            
    def tearDown(self):
        self.drive.quit()
        self.assertEqual([],self.verificationErrors)
            
if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(BaiduTest'')


          
            