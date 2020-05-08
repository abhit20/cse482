#!/usr/bin/python
import sys

attributes = ["preg", "plas", "pres", "skin", "insu", "mass", "pedi", "age"]

for myline in sys.stdin: 
	words = myline.split(',')
	for i in range(0,len(attributes)):
		j = i + 1
		while j<len(attributes):
			keyTup = (attributes[i],attributes[j])
			valueTup = (words[i],words[j])
			print '%s\t%s' % (keyTup,valueTup)
			j+=1
