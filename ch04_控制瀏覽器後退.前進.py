from selenium import webdriver

drive = webdriver.Chrome()

first_url = 'https://www.google.com.tw/?gfe_rd=cr&ei=iMauVqrHMcGG2QSF26OABA&gws_rd=ssl'
second_url = 'https://edition.cnn.com/'

print("Now access first url")
drive.get(first_url)


print("Now access second url")
drive.get(second_url)

print("Now back Google")
drive.back()

print("Now foword News web")
drive.forward()