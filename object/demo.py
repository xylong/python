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




linlin = Wife('琳琳', 18)
xixi = Lover('西西', 17)


# 多态
def sleep(girl):
	girl.sleep()

l = [girl, linlin, xixi]
for u in l:
	sleep(u)


h = Harem([girl, linlin, xixi])
h.count()
h.show()