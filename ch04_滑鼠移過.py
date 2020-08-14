from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

drive = webdriver.Chrome()
drive.get("https://www.google.com.tw/?gfe_rd=cr&ei=iMauVqrHMcGG2QSF26OABA&gws_rd=ssl")

above = drive.find_element_by_name('q')
ActionChains(drive).move_to_element(above).perform()
