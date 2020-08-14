from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.google.com.tw/?gfe_rd=cr&ei=iMauVqrHMcGG2QSF26OABA&gws_rd=ssl')

enter_email = driver.find_element_by_id('gb_70')
ActionChains(driver).click(enter_email).perform()

title = driver.title
print(title)

Identafy = driver.find_element_by_id('identifierId')
Identafy.send_keys("aeabom741@gmail.com")

log_buttom = driver.find_element_by_class_name('VfPpkd-RLmnJb')
ActionChains(driver).click(log_buttom).perform()
sleep(3)

url = driver.current_url
print(url)