from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Page(object):
    """
    基礎類別，用於頁面物件類別的繼承
    """
    login_url = 'https://www.facebook.com'
    
    def __init__(self,selenium_drive,base_url = login_url):
        self.base_url = base_url
        self.drive = selenium_drive
        self.timeout = 30
        
    def on_page(self):
        return self.drive.current_url == (self.base_url + self.url)
    
    def _open(self,url):
        url = self.base_url + url
        self.drive.get(url)
        assert self.on_page(), 'Did not land on %s' %url
        
    def open(self):
        self._open(self.url)
        
    def find_element(self,*loc):
        return self.drive.find_element(*loc)
    
class LoginPage(Page):
    """
    FB登入頁面模型
    """
    url ='/'
    username_loc = (By.NAME,'email')
    password_loc = (By.NAME,'pass')
    submit_loc = (By.NAME,'login')
    
    def type_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)
    
    def type_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)
    
    def submit(self):
        self.find_element(*self.submit_loc).click()
        
def test_user_login(drive, username, password):
    login_page = LoginPage(drive)
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()
    
def main():
    try:
        drive = webdriver.Chrome()
        username = 'username'
        password = '123456'
        test_user_login(drive,username,password)
        sleep(3)
    finally:
        drive.close()
        
if __name__ == '__main__':
    main()