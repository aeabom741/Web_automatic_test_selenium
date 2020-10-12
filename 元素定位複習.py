from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

drive = webdriver.Chrome()
drive.get('https://www.google.com.tw/?gfe_rd=cr&ei=iMauVqrHMcGG2QSF26OABA&gws_rd=ssl')
drive.implicitly_wait(30)

print('search element find by name')
name = drive.find_element_by_name('q')
name.send_keys('selenium')
print('submit element find by class name')
submit = drive.find_element_by_class_name('gNO89b')
submit.click()
drive.back()
sleep(3)

print('search element find by xpath')
xpath = drive.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
xpath.send_keys('webdrive')
print('submit element find by name')
submit = drive.find_element_by_name('btnK')
submit.click()
drive.back()
sleep(3)

print('search element find by Xpath_class_name')
xpath_class = drive.find_element_by_xpath('//input[@class="gLFyf gsfi"]')
xpath_class.send_keys('go')
print('submit element find by Xpath')
submit = drive.find_element_by_xpath('//input[@value="Google 搜尋"]')
submit.click()
drive.back()
sleep(3)


"""
email account
"""

print('find login element by Xpath')
login = drive.find_element_by_xpath('//a[@id="gb_70"]')
login.click()

print('find account element by id')
account = drive.find_element_by_id('identifierId')
account.send_keys('aeabom')
sleep(3)
account.clear()

print('find account element by Xpath')
account = drive.find_element_by_xpath('//input[@class="whsOnd zHQkBf"]')
account.send_keys('swiftlock')
sleep(3)

print('find login button element by class name')
submit = drive.find_element_by_class_name('VfPpkd-RLmnJb')
submit.click()
sleep(3)

drive.back()
drive.back()
sleep(3)

drive.quit()