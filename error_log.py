#!/usr/bin/env python
#actor: day
#func: sort error log
#time: 4-02-2016
#####################

import sys
error_log_path=sys.argv[1]
class Error(object):
	def __init__(self,error_log_path):
		self.error_log_path = error_log_path

	def count(self):
		li = []
		f = open(self.error_log_path,'r')
		for i in f:
			li.append(i)
			if len(li) <= 6:
				if i.find('error') != -1:
					for i in range(len(li)):
						print li[i],
					print '#'*10+ '\n'
			else:
				del li[0]
				if i.find('error') != -1:
					for i in range(len(li)):
						print li[i],
					print '#'*10 + '\n'
		f.close()
error = Error(error_log_path)
error.count()
