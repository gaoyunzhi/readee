#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import readee
import os
import sys

urls = [
	'https://zh.wikipedia.org/zh-cn/%E6%98%A5%E8%95%BE%E8%AE%A1%E5%88%92',
]

def getFileName(url):
	os.system('mkdir result > /dev/null 2>&1')
	name = url.split('/')[-1]
	name = name.split('.')[0]
	return 'result/%s.html' % name

def test():
	if len(sys.argv) > 1:
		mode = sys.argv[1]
	else:
		mode = ''
	if mode == 'open':
		mode = ''
	for url in urls:
		if not mode in url:
			continue
		print('原文：', url)
		name = getFileName(url)
		with open(name, 'w') as f:
			f.write(readee.export(url))
		print('导出：', r)
		if 'open' in str(sys.argv):
			os.system('open ' + name + ' -g')

test()