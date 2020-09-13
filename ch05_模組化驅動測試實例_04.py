from selenium import webdriver
from public2 import Login

class LoginTest():
    
    def __init__(self):
        self.drive = webdriver.Chrome()
        self.drive.get('https://www.facebook.com/?stype=lo&jlou=AffuPJ79S6_XWLhj_8ugqbvD2inXkN6OXA2Zb2s_zSEcR6IOFwd52qBpsz7-VuU2S5b6ka-c1Q528d8KgcpB_j-G2WLdanTLLzw63g6AIswjVg&smuh=33167&lh=Ac_vSFVID15q10Vp')
        self.drive.implicitly_wait(15)
        
    def test_login1(self):
        
        username = 'aeabom'
        password = '12345'
        Login().user_login(self.drive,username,password)
        Login().user_login_out(self.drive)
    def test_login2(self):
        
        username = 'aeabon789'
        password = '123658'      
        Login().user_login(self.drive, username,password)
        Login().user_login_out(self.drive)

LoginTest().test_login1()
LoginTest().test_login2()       