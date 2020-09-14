from xml.dom import minidom

dom = minidom.parse('info.xml')

province = dom.getElementsByTagName('province')
city = dom.getElementsByTagName('city')

p0 = province[0].firstChild.data
print(p0)

p1 = province[1].firstChild.data
print(p1)

c2 = city[2].firstChild.data
print(c2)