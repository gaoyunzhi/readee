#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import readee
import os
import sys

urls = [
	'https://medium.com/@moreless/%E4%BB%8E%E6%94%BB%E5%A3%B3%E6%9C%BA%E5%8A%A8%E9%98%9F%E7%9C%8B%E4%B8%BA%E4%BA%86%E8%AE%A1%E7%AE%97%E6%9C%BAio%E5%8F%91%E5%B1%95%E7%9A%84%E6%96%B9%E5%90%91-e923d2368541'
]

def getFileName(url):
	os.system('mkdir result > /dev/null 2>&1')
	name = [x for x in url.split('/') if x][-1]
	name = [x for x in name.split('.') if x][0]
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
			f.write(str(readee.export(url, toSimplified=True)))
		print('导出：', name)
		if 'open' in str(sys.argv):
			os.system('open ' + name + ' -g')

if __name__=='__main__':
	test()