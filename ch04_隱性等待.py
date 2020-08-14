from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import ctime

drive = webdriver.Chrome()

drive.implicitly_wait(10)
drive.get('https://www.google.com.tw/?gfe_rd=cr&ei=iMauVqrHMcGG2QSF26OABA&gws_rd=ssl')


try:
    print(ctime())
    drive.find_element_by_name('q').send_keys("Selenium")
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
    drive.quit()
    