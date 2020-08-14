from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

drive = webdriver.Chrome()
drive.get('https://www.google.com.tw/?gfe_rd=cr&ei=iMauVqrHMcGG2QSF26OABA&gws_rd=ssl')

logo = drive.find_element_by_link_text('廣告')
ActionChains(drive).double_click(logo).perform()