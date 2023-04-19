import csv

with open('myfile.csv', mode ='r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)
print('*************************************************')

with open('myfile.csv', mode ='r') as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        print(lines)