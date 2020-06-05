#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import readee
import os
import sys

urls = [
	'https://gravitysworm.com/post/618739126459678720/%E7%96%AB%E6%83%85%E4%B8%8B%E7%9A%84%E7%A4%BE%E4%BC%9A%E8%BF%90%E5%8A%A8%E7%89%88%E5%9B%BE%E6%94%B6%E7%BC%A9%E5%80%92%E6%8C%82%E4%B8%8E%E9%87%8D%E5%90%AF'
]

def getFileName(url):
	os.system('mkdir result > /dev/null 2>&1')
	name = [x for x in url.split('/') if x][-1]
	name = [x for x in name.split('.') if x][0]
	return 'result/%s.html' % name[:20]

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
			f.write(str(readee.export(url, toSimplified=False)))
		print('导出：', name)
		if 'open' in str(sys.argv):
			os.system('open ' + name + ' -g')

if __name__=='__main__':
	test()