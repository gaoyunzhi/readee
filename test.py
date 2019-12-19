#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import readee
import os
import sys

urls = [
	'https://thestir.cafemom.com/parenting_news/220907/felicia-saunders-moms-photo-shoot-fed-is-best/308747/pin_it/9?utm_medium=Facebook&utm_source=LTcom&fbclid=IwAR0XrrDVPTiWg2Eenxoy-8yXNxB2HSBIhFIYsjQm4A215EGugbNSkMjJLp8',
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
			f.write(str(readee.export(url, include_title=True)))
		print('导出：', name)
		if 'open' in str(sys.argv):
			os.system('open ' + name + ' -g')

test()