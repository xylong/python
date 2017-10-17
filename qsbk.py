#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-16 15:55:47
# @Author  : xyl (416319808@qq.com)
# @Link    : https://github.com/xylong
# @Version : 1.1

from urllib import request
import re


class QSBK(object):
	"""糗事百科爬虫"""
	def __init__(self):
		self.enable = False
		self.stories = []
		self.paegIndex = 1
		self.url = 'https://www.qiushibaike.com/hot/page/'
		self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
		self.reg = re.compile('''<div class="article block untagged mb15.*?<h2>(.*?)</h2>'''
						 + '''.*?<span>(.*?)</span>'''
						 + '''.*?<!-- 图片或gif -->(.*?)<div class="stats">'''
						 +'''.*?<span class="stats-vote"><i class="number">(.*?)</i>''', re.S)

	# 获取页面代码
	def getPage(self, paegIndex):
		'''根据页码获取页面内容'''
		url = self.url + str(paegIndex)
		req = request.Request(url)
		req.add_header('User-Agent', self.user_agent)

		with request.urlopen(req) as f:
			if f.status == 200:
				return f.read().decode('utf-8')


	# 获取当前页段子				
	def getStains(self, paegIndex = 1):
		'''返回不带图的段子列表'''
		pageCode = self.getPage(paegIndex)

		if not pageCode:
			print('页面加载失败...')
			return None

		res = re.findall(self.reg, pageCode)
		stains = []

		for stain in res:
			if not re.search('img', stain[2]):
				replaceBR = re.compile('<br/>')
				text = re.sub(replaceBR, '\n', stain[1])
				stains.append([stain[0].strip(), text.strip(), stain[2].strip(), stain[3].strip()])
		return stains

	# 加载并提取页面的内容
	def loadPage(self):
		if self.enable == True:
			# 如果当前未看的页数少于2页，则加载新一页
			if len(self.stories) < 2:
				# 获取新一页
				stories = self.getStains(self.paegIndex)
				if stories:
					self.stories.append(stories)
					self.paegIndex += 1

	# 每次打印一个段子					
	def getOne(self, stains, page):
		for stain in stains:
			_input = input()
			self.loadPage()
			if _input == 'q':
				self.enable = False
				return
			print('当前第:%s页\n发布人:%s\n内容:%s\n点赞数:%s\n' % (page, stain[0], stain[1], stain[3]))


	def start(self):
		print('正在读取糗事百科，按回车查看新段子，q退出')
		self.enable = True
		self.loadPage()
		nowPage = 0
		while self.enable:
			if len(self.stories) > 0:
				stories = self.stories[0]
				nowPage += 1
				del self.stories[0]
				self.getOne(stories, nowPage)


qs = QSBK()
qs.start()
