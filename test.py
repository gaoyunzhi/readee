#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import readee
import os
import sys

urls = [
	'https://www.twreporter.org/a/opinion-covid-19-reflect-public-health-problem?utm_source=telegram&utm_medium=telegram&utm_campaign=telegram'
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