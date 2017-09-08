#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: woman.py

from girl import Girl

class Wife(Girl):
	"""妻子"""
	def __init__(self, name, age = 0):
		super().__init__(name, age)

	def marry(self):
		print('married')

	def sleep(self):
		print('sleep with wife')



class Lover(Girl):
	"""情人"""
	def __init__(self, name, age = 0):
		super().__init__(name, age)

	def sleep(self):
		print('sleep with lovers')



class Harem(object):
	"""后宫"""
	wifes = []
	lovers = []

	def __init__(self, users):
		if isinstance(users, list):
			for u in users:
				if isinstance(u, Wife):
					self.wifes.append(u)
				else:
					self.lovers.append(u)


	def count(self):
		print('你有%d个老婆，%d个情人' % (len(self.wifes), len(self.lovers)))

	def show(self):
		'分类显示后宫'
		print('你的老婆有：%s \n你的情人有：%s' % (self.getUser(self.wifes), self.getUser(self.lovers)))

	def getUser(self, arr):
		'根据不同后宫类型查找'
		return '、'.join(list(map(lambda u: u.name, arr)))