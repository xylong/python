#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: woman.py

from girl import Girl

class Wife(Girl):
	"""妻子"""
	def __init__(self, name, age):
		super().__init__(name, age)


	def marry():
		print('married')



class Lover(object):
	"""情人"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		