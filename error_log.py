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
	for i in f:
		li.append(i)
		if len(li) <= 6:
			if i.find('error') != -1:
				for i in range(len(li)):
					print li[i],
				print '###############\n'
		else:
			del li[0]
			if i.find('error') != -1:
				for i in range(len(li)):
					print li[i],
				print '###############\n'
	f.close()

count(error_log_path)
