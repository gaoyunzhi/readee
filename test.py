#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import readee
import os
import sys

urls = [
	'https://matters.news/@HollowErhu/matters%E7%A4%BE%E5%8D%80%E6%B4%BB%E5%8B%95%E6%8F%90%E6%A1%88-%E6%88%91%E5%B9%B3%E5%B8%B8%E9%83%BD%E7%9C%8B%E4%BB%80%E9%BA%BC%E6%9B%B8-%E5%BE%B5%E6%96%87%E6%B4%BB%E5%8B%95-bafyreibzedplnny5aagm3sw66bj3n6wtozj7ndq53ol5mkhfp2qtmmshza'
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
			f.write(str(readee.export(url, include_title=True, move_head_photo=True, toSimplified=True)))
		print('导出：', name)
		if 'open' in str(sys.argv):
			os.system('open ' + name + ' -g')

if __name__=='__main__':
	test()