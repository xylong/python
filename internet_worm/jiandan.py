#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-11 16:10:15
# @Author  : xyl (416319808@qq.com)
# @Link    : https://github.com/xylong
# @Version : $Id$

from urllib import request
import os

def url_open(url):
	req = request.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
	response = request.urlopen(url)
	html = response.read()
	return html


def get_page(url):
	html = url_open(url).decode('utf-8')

	a = html.find('current-comment-page') + 23
	b = html.find(']', a)
	return html[a:b]


def find_imgs(url):
	html = url_open(url).decode('utf-8')
	img_addrs = list()

	a = html.find('img src')

	while a != -1:
		b = html.find('.jpg', a, a + 255)
		if b != -1:
			img_addrs.append('http:' + html[a + 9:b + 4])
		else:
			b = a + 9
		a = html.find('img src=', b)

	return img_addrs

def save_imgs(folder, img_addrs):
	for pic in img_addrs:
		filname = pic.split('/')[-1]
		with open(filname, 'wb') as f:
			img = url_open(pic)
			f.write(img)


def download_mm(folder = 'ooxx', pages = 10):
	os.chdir(folder)

	url = 'http://jandan.net/ooxx/'
	page_num = int(get_page(url))

	for i in range(pages):
		page_num -= i
		page_url = url + 'page' + str(page_num) + '#comments'
		img_addrs = find_imgs(page_url)
		save_imgs(folder, img_addrs)


if __name__ == '__main__':
	download_mm()