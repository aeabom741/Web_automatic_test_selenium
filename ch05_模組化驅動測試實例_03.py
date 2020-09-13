from selenium import webdriver
from public import Login

drive = webdriver.Chrome()
drive.get('https://www.facebook.com/?stype=lo&jlou=AffuPJ79S6_XWLhj_8ugqbvD2inXkN6OXA2Zb2s_zSEcR6IOFwd52qBpsz7-VuU2S5b6ka-c1Q528d8KgcpB_j-G2WLdanTLLzw63g6AIswjVg&smuh=33167&lh=Ac_vSFVID15q10Vp')
drive.implicitly_wait(10)

Login().user_login(drive)
Login().user_login_out(drive)