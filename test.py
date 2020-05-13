#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import readee
import os
import sys

urls = [
	'https://mp.weixin.qq.com/s?src=11&timestamp=1589384869&ver=2336&signature=sTeeoWaZ2MzuU6mNg5iC*5iZbXBQJLcsg1mnnBX*2tjQkLJUzWAQVlgM7ZwuZNyqmT3RuNpxoqnnonX-X8Jl6RQK008PWGQqq70XvQC9A*v6BMyH5OKKdIq3ue0msJJo&new=1'
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