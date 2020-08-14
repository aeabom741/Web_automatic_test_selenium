from selenium import webdriver
from time import sleep, ctime

drive = webdriver.Chrome()
drive.get('https://www.google.com.tw/?gfe_rd=cr&ei=iMauVqrHMcGG2QSF26OABA&gws_rd=ssl')
print(ctime())
for i in range(10):
    try:
        el = drive.find_element_by_name('q')
        if el.is_displayed():
            break
    except: pass
    sleep(1)
else:
    print("Time out")
drive.close()
print(ctime())