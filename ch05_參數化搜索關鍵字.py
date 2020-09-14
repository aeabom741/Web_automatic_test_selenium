from selenium import webdriver
import time as t
search_text = ['python' , ' 中文' , 'text']

for text in search_text:
    
    drive = webdriver.Chrome()
    drive.get('https://www.baidu.com/')
    drive.implicitly_wait(10)
    drive.find_element_by_id('kw').send_keys(text)
    drive.find_element_by_id('su').click()
    t.sleep(3)
    drive.quit()