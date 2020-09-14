from xml.dom import minidom

dom = minidom.parse('info.xml')

login = dom.getElementsByTagName('login')

username = login[0].getAttribute('username')
print(username)
password = login[0].getAttribute('password')
print(password)

username = login[1].getAttribute('username')
print(username)
password = login[1].getAttribute('password')
print(password)