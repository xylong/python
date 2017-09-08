#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: demo.py

from woman import *

# 测试Girl
girl = Girl('静静', 18)

# 私有属性不能直接搞
try:
	print(girl.__age)
except Exception as e:
	print('私有属性不能直接搞:', e)
finally:
	print(girl.age, girl.getAge(), girl._Girl__age)
