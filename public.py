class Login():
    def user_login(self,drive):
        drive.find_element_by_name('email').clear()
        drive.find_element_by_name('email').send_keys('aeabom')
        
        drive.find_element_by_name('pass').clear()
        drive.find_element_by_name('pass').send_keys('12345')
        
        drive.find_element_by_name('login').click()
        import time as t
        t.sleep(5)
        
    def user_login_out(self,drive):
        drive.quit()