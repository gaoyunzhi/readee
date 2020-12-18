#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import readee
import os
import sys

urls = [
	'https://www.greenpeace.org/taiwan/update/22392/%e5%85%a8%e7%90%83%e8%88%87%e6%9d%b1%e4%ba%9e%e5%90%84%e5%9c%b0%e9%99%b8%e7%ba%8c%e5%ae%a3%e5%b8%83%e7%a2%b3%e4%b8%ad%e5%92%8c%e7%9b%ae%e6%a8%99%ef%bc%8c%e8%87%ba%e7%81%a3%e5%88%a5%e5%9c%a8%e5%b0%8d/?ref=optimonk_post_link'
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