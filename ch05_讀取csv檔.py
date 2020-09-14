import csv

data = csv.reader(open('info.csv','r'))

for user in data:
    print(user[1])