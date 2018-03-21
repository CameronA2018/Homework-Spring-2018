import csv
import time

roster = open("roster.csv", "rb")
for line in csv.reader(roster):
	if not line:
		empty_lines += 1
		continue
		print line[0]
