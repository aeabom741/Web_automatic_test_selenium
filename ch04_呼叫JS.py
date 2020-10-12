from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

drive = webdriver.Chrome()
drive.get('https://www.google.com/webhp?source=search_app')
WebDriverWait(drive,5,0.5).until(EC.presence_of_element_located\
             ((By.XPATH,'//input[@class = "gLFyf gsfi"]')))

selection = drive.find_element(By.XPATH,'//div[@class = "gb_Uf"]')
selection.click()

drive.switch_to_frame(0)
new = drive.find_element(By.LINK_TEXT,'新聞')
new.click()

WebDriverWait(drive,5,0.5).until(EC.presence_of_element_located((By.XPATH,\
             '//input[@class = "Ax4B8 ZAGvjd"]')))
print('OK')

js = "window.scrollTo(100,800);"#呼叫JAVA SCRIP
drive.execute_script(js)
sleep(3)
drive.quit()