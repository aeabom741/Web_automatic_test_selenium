from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

drive = webdriver.Chrome()
drive.get('https://www.google.com.tw/?gfe_rd=cr&ei=iMauVqrHMcGG2QSF26OABA&gws_rd=ssl')

element = WebDriverWait(drive,5,0.5).until(ec.presence_of_element_located((By.NAME, 'q')))
element.send_keys('Selenium')
drive.quit()