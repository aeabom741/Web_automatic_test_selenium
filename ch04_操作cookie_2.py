from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

drive = webdriver.Chrome()
drive.get('https://www.google.com/webhp?source=search_app')
WebDriverWait(drive,5,0.5).until(EC.presence_of_element_located\
             ((By.XPATH,'//input[@class = "gLFyf gsfi"]')))

for cookie in drive.get_cookies():
    print("%s -> %s" %(cookie['name'],cookie['value']))
    
drive.quit()