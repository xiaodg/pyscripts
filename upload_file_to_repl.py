#coding:utf-8

import os
import sys
import requests

if len(sys.argv)>1:
	file_list = sys.argv[1:]
	for file in file_list:
		if os.path.exists(file) and (not os.path.isdir(file)):
			url = 'http://dj--xiaodg.repl.co/files'
			files = {'file': open(file,'rb')}
			r = requests.post(url, files=files)
		else:
			print("指定路径%s不存在或者为目录" % file)