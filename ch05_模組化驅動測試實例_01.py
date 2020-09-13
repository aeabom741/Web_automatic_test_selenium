from selenium import webdriver
import time as t
drive = webdriver.Chrome()
drive.get('https://www.facebook.com/?stype=lo&jlou=AffuPJ79S6_XWLhj_8ugqbvD2inXkN6OXA2Zb2s_zSEcR6IOFwd52qBpsz7-VuU2S5b6ka-c1Q528d8KgcpB_j-G2WLdanTLLzw63g6AIswjVg&smuh=33167&lh=Ac_vSFVID15q10Vp')
drive.implicitly_wait(10)

#登入
drive.find_element_by_name('email').clear()
drive.find_element_by_name('email').send_keys('aeabom')
drive.find_element_by_name('pass').clear()
drive.find_element_by_name('pass').send_keys('Aazz011105')
drive.find_element_by_name('login').click()

t.sleep(6)
drive.quit()