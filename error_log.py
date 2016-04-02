#!/usr/bin/env python
#actor: day
#func: sort error log
#time: 4-02-2016
#####################

import sys

error_log_path=sys.argv[1]

def count(error_log_path):
	li = []
	f = open(error_log_path,'r')
	lines = len(f.readlines())
	f.seek(0,0)
	for i in range(lines):
		li.append(line)
		if len(li) <= 6:
			if line.find('error') != -1:
				for i in range(len(li)):
					print li[i],
				print '###############\n'
		else:
			del li[0]
			if line.find('error') != -1:
				for i in range(len(li)):
					print li[i],
				print '###############\n'
	f.close()

count(error_log_path)
