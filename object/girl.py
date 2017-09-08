#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Girl(object):
	"""妹子"""
	name = ''
	__age = 0	# 私有属性(伪私有)，实际上python自动改成_类名__属性名

	def __init__(self, name, age):
		self.name = name
		self.__age = age

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


class Wife(Girl):
	"""妻子"""
	def __init__(self, name):
		super().__init__()
		self.name = name

class Lover(object):
	"""情人"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		

girl = Girl('jingjing', 108)
print(girl.getAge())
print(girl.name)
girl.age = 19
print(girl.age, girl.getAge(), girl._Girl__age)	# 三种取法

# 私有属性不能直接搞
try:
	print(girl.__age)
except AttributeError as e:
	print(e)