from selenium import webdriver

drive = webdriver.Chrome()
drive.get('https://www.google.com.tw/?gfe_rd=cr&ei=iMauVqrHMcGG2QSF26OABA&gws_rd=ssl')

drive.find_element_by_name("q").send_keys("Hello")
drive.find_element_by_name("q").submit()

drive.quit()