from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

drive = webdriver.Chrome()
drive.get("https://www.google.com.tw/?gfe_rd=cr&ei=iMauVqrHMcGG2QSF26OABA&gws_rd=ssl")

right_click = drive.find_element_by_name('q')
ActionChains(drive).context_click(right_click).perform()
