#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: girl.py

class Girl(object):
	"""妹子"""
	name = ''
	__age = 0	# 私有属性(伪私有)，实际上python自动改成_类名__属性名

	def __init__(self, name, age = 0):
		self.name = name
		if isinstance(age, int):
			self.setAge(age)

	def getAge(self):
		'获取年龄'
		return self.__age

	def setAge(self, age):
		'设置年龄'
		if not isinstance(age, int):
			raise ValueError('age must be an integer')
		if age < 0 or age > 100:
			raise ValueError('age must between 0~100')
		self.__age = age

	def delAge():
		'删除年龄'
		del __age

	age = property(getAge, setAge, delAge)	# 方法转属性

	def sleep(self):
		print('sleep with a girl')

