import csv

with open('roster.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		name = row[0]
		realName = name.isdigit()
		print (name)
