#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import readee
import os
import sys

urls = [
	'https://matters.news/@bash99/%E5%86%85%E5%AE%B9%E7%A4%BE%E5%8C%BA%E6%98%AF%E5%90%A6%E4%B8%A2%E5%A4%B1%E4%BA%86%E8%AE%BA%E5%9D%9B%E7%9A%84%E6%9F%90%E4%BA%9B%E4%BC%98%E7%82%B9-bafyreifeow5eax7al6kzc62tfayg7eat6o3vgrlnhojbofhn7ldltjdzw4'
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