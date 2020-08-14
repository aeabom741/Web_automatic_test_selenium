from selenium import webdriver
drive = webdriver.Chrome()
drive.get('https://www.google.com.tw/?gfe_rd=cr&ei=iMauVqrHMcGG2QSF26OABA&gws_rd=ssl')

size = drive.find_element_by_name("q").size
print("輸入框尺寸%s" %size)

text = drive.find_element_by_class_name("Q8LRLc").text
print("底部字串:%s" %text)

result = drive.find_element_by_class_name("fbar").is_displayed()
print(result)

drive.quit()
