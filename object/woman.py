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
	def __init__(self, wifes, lovers):
		self.wifes = wifes
		self.lovers = lovers

	def count(self):
		print('你有%d个老婆，%d个情人' % (len(self.wifes), len(self.lovers)))