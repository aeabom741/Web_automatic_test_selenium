from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
drive = webdriver.Chrome()
drive.get("https://www.google.com.tw/?gfe_rd=cr&ei=iMauVqrHMcGG2QSF26OABA&gws_rd=ssl")

input_1 =drive.find_element_by_name('q') 

input_1.send_keys("Seleniume")
input_1.send_keys(Keys.BACK_SPACE)
sleep(1)

input_1.send_keys(Keys.SPACE)
input_1.send_keys("教學")
sleep(1)

input_1.send_keys(Keys.CONTROL, 'a')
input_1.send_keys(Keys.CONTROL, 'c')
input_1.send_keys(Keys.CONTROL, 'v')
sleep(1)

input_1.submit()
