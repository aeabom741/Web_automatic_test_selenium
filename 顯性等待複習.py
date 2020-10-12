from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep

drive = webdriver.Chrome()
drive.get('https://www.google.com/webhp?source=search_app') 
WebDriverWait(drive,5,0.5).until(EC.presence_of_element_located((By.XPATH\
             ,'//input[@class = "gLFyf gsfi"]')),"OK!")

selection = drive.find_element(By.XPATH,'//a[@class="gb_D gb_wc"]')
selection.click()

drive.switch_to_frame(0)
WebDriverWait(drive,5,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,\
             '新聞')))
new = drive.find_element(By.LINK_TEXT,'新聞')
new.click()
sleep(1)

WebDriverWait(drive,5,0.5).until(EC.presence_of_element_located((By.XPATH,\
             '//input[@class = "Ax4B8 ZAGvjd"]')))
search = drive.find_element(By.XPATH,'//input[@class = "Ax4B8 ZAGvjd"]')
search.send_keys('諾貝爾獎')
sleep(1)

button = drive.find_element(By.XPATH,'//button[@class = "gb_yf"]')
button.click()
sleep(1)


drive.get('https://www.google.com/webhp?source=search_app')
WebDriverWait(drive,5,0.5).until(EC.presence_of_element_located((By.XPATH,\
             '//a[@id = "gb_70"]')))
sleep(1)

login = drive.find_element(By.XPATH,'//a[@id = "gb_70"]')
login.click()
sleep(1)

account = drive.find_element(By.XPATH,'//input[@class = "whsOnd zHQkBf"]')
account.send_keys('aeabom741@gmail.com')
sleep(1)

button = drive.find_element(By.XPATH,'//div[@class = "VfPpkd-RLmnJb"]')
button.click()
sleep(1)

drive.get('https://www.google.com/webhp?source=search_app')
WebDriverWait(drive,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//input[@class = "gLFyf gsfi"]')))
print("OK")