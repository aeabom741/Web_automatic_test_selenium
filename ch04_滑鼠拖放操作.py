from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

drive = webdriver.Chrome()
drive.get('https://www.google.com.tw/?gfe_rd=cr&ei=iMauVqrHMcGG2QSF26OABA&gws_rd=ssl')

element = drive.find_element_by_name("q")

target = drive.find_element_by_name("q")
ActionChains(drive).drag_and_drop(element,target).perform()