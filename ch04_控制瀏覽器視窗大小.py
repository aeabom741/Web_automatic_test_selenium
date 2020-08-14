from selenium import webdriver

drive = webdriver.Chrome()
drive.get("https://www.google.com.tw/?gfe_rd=cr&ei=iMauVqrHMcGG2QSF26OABA&gws_rd=ssl")

#參數為像數值
print("寬400 高800")
drive.set_window_size(400,800)
drive.quit()