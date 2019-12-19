#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import readee
import os
import sys

urls = [
	'https://thestir.cafemom.com/parenting_news/220907/felicia-saunders-moms-photo-shoot-fed-is-best/307364/saunders_left_that_experience_with_a_valuable_lesson_that_what_is_best_for_my_child_and_i_is_not_always_what_may_be_best_for_the_next_family/4',
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