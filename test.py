#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import readee
import os
import sys

urls = [
	'https://mp.weixin.qq.com/s?__biz=MzI2MTExMTE3Ng==&amp;mid=2247483688&amp;idx=1&amp;sn=4f1146d79e1d37aa23c61467c876c2a2&amp;chksm=ea5e2dcfdd29a4d96243437cd6f4109925c4e70592e34e12039500c5917412d25174c9d3e885&amp;mpshare=1&amp;scene=1&amp;srcid=&amp;sharer_sharetime=1587789413659&amp;sharer_shareid=7c19efe830ee0c8a2796cbc54e04c282#rd'
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
			f.write(str(readee.export(url)))
		print('导出：', name)
		if 'open' in str(sys.argv):
			os.system('open ' + name + ' -g')

if __name__=='__main__':
	test()