class Login():
    def user_login(self ,drive ,username ,password):
        import time as t
        drive.find_element_by_name('email').clear()
        drive.find_element_by_name('email').send_keys(username)
        
        drive.find_element_by_name('pass').clear()
        drive.find_element_by_name('pass').send_keys(password)
        
        drive.find_element_by_name('login').click()
        t.sleep(5)
        
    def user_login_out(self,drive):
        drive.quit()
    