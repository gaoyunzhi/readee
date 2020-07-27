#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import readee
import os
import sys

urls = [
	'https://chinadigitaltimes.net/chinese/2016/11/%E6%B3%95%E6%84%8F%E7%BC%96%E8%AF%91-%E9%A9%AC%E5%85%8B%E2%80%A2%E9%87%8C%E6%8B%89%EF%BC%9A%E8%BA%AB%E4%BB%BD%E8%87%AA%E7%94%B1%E4%B8%BB%E4%B9%89%E7%9A%84%E7%BB%88%E7%BB%93/'
]

def getFileName(url):
	os.system('mkdir result > /dev/null 2>&1')
	name = [x for x in url.split('/') if x][-1]
	name = [x for x in name.split('.') if x][0]
	return 'result/%s.html' % name[:20]

def test():
	for url in urls:
		print('原文：', url)
		name = getFileName(url)
		with open(name, 'w') as f:
			f.write(str(readee.export(url, toSimplified=False)))
		print('导出：', name)
		os.system('open ' + name + ' -g')

if __name__=='__main__':
	test()