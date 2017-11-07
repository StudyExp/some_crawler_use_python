# coding=utf-8
# 用来统计代码行数

import os
import time

basedir = '../'
filelists = []
whitelist = ['md']


def getFile(basedir):
	'''
	getFile
	'''
	global filelists

	for parent, dirnames, filenames in os.walk(basedir):
		
		for filename in filenames:
	
			ext = filename.split('.')[-1]
			if ext in whitelist:
				filelists.append(os.path.join(parent, filename))


def countLine(fname):
	count = 0
	for file_line in open(fname).readlines():
		
		if file_line != '' and file_line != '\n':
			count += 1

		print(fname + '---', count)

	return count


if __name__ == '__main__':
	starttime = time.clock()
	getFile(basedir)
	totalline = 0

	print(filelists)

	global filelists

	for filelist in filelists:
		totalline = totalline + countLine(filelist)

	print('total lines:', totalline)
	print('Done! Cost Time: %0.2f second' % (time.clock() - starttime))
