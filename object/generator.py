#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-11 13:31:27
# @Author  : xyl (416319808@qq.com)
# @Link    : https://github.com/xylong
# @Version : 1.1

class Libs(object):
	"""斐波拉契数列"""
	def __init__(self, n):
		self.n = n
		self.a = 0
		self.b = 1

	def __iter__(self):
		return self

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > self.n:
			raise StopIteration
		return self.a

f = Libs(20)
for x in f:
	print(x)


def lib(n):
	'获取n以内斐波拉契数列'
	a = 0
	b = 1
	while True:
		a, b = b, a + b
		if a > n:
			break
		yield a

res = lib(20)
for x in res:
	print(x)
