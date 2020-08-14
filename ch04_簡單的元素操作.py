from selenium import webdriver

drive = webdriver.Chrome()
drive.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

drive.find_element_by_id("identifierId").clear()
drive.find_element_by_id("identifierId").send_keys("aeabom741")

drive.find_element_by_class_name("VfPpkd-RLmnJb").click()