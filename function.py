#!/usr/bin/env python3
# -*- coding: utf-8 -*-




def area(width):
	'闭包案例1'
	def calculation(height):
		return width * height
	return calculation

def func(x):
	'闭包案例2'
	def fun():
		nonlocal x
		x *= x
		return x
	return fun()

g = lambda x : x * 2 + 1

# print(area(7)(8))
# print(func(6))
# print(g(5))

print(list(filter(lambda x : x % 2, range(10))))	# filter
print(list(map(lambda x : x**2, range(1, 10, 2))))	# map


def factorial1(n):
	'非递归版阶乘'
	result = n
	for i in range(1, n):
		result *= i
	return result

def factorial2(n):
	'递归阶乘'
	if n == 1:
		return 1
	return n * factorial2(n - 1)

print(factorial1(5))
print(factorial2(5))
