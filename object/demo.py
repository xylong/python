#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: demo.py

from woman import *
import girl

# 测试对象特性
girl = girl.Girl('静静', 20)

# 私有属性不能直接搞
try:
	print(girl.__age)
except Exception as e:
	print('私有属性不能直接搞:', e)
finally:
	print(girl.age, girl.getAge(), girl._Girl__age)




wife = Wife('琳琳', 18)
wife.marry()
