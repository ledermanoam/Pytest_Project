import csv
import rows

import rows as rows

with open('myfile.csv', mode ='r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)
print('*************************************************')

with open('myfile.csv', mode ='r') as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        print(lines)

print("**************************************************")

rows = []
with open('myfile.csv', mode ='r') as file:
    csvFile = csv.reader(file)
    header = next(csvFile)
    for lines in csvFile:
        rows.append(lines)


print(rows)
for row in rows:
    print(row)
