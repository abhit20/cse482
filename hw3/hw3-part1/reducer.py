#!/usr/bin/python
import sys
import math

def correlation(arr):
	sumX = 0
	sumY = 0
	sumXY = 0
	sumXsquared = 0
	sumYsquared = 0

	count = 1
	for tup in arr:
		sumX += float(tup[0])
		sumY += float(tup[1])


		sumXY += (float(tup[0]) * float(tup[1]))
		sumXsquared += (float(tup[0]) * float(tup[0]))
		sumYsquared += (float(tup[1]) * float(tup[1]))
		count += 1
	corr = (count * sumXY - sumX * sumY) / (math.sqrt(count * sumXsquared -  (sumX * sumX)) * math.sqrt(count * sumYsquared - (sumY * sumY)))

	return corr


prev_key = '999999'
arr = []
count = 0

for myline in sys.stdin: 
	myline = myline.strip() 
	words = myline.split('\t')

	if prev_key != words[0] and count == 0:
		prev_key = words[0]
		count += 1
	elif prev_key != words[0] and count != 0:
		print "%s\t%s" % (prev_key, correlation(arr))
		prev_key = words[0]
		arr = []
	elif prev_key == words[0]:
		tup = ((words[1].replace('(','')).replace(')','')).replace("'","")
		tup = tuple(tup.split(','))
		arr.append(tup)

print "%s\t%s" % (prev_key, correlation(arr))