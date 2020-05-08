#!/usr/bin/python
import sys

prev_key = '999999'
count = 0
maximum = -9999999
model = ""
for myline in sys.stdin: 
	myline = myline.strip() 
	words = myline.split('\t') 
	if prev_key != words[0]:
            if prev_key != '999999' :
                print "%s\t%s" % (prev_key, maximum)
            maximum = 0
        prev_key = words[0]
        if words[1] != "?":
            if maximum < float(words[1]):
                maximum = float(words[1])

print "%s\t%s" % (words[0], maximum)
