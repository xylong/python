#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-17 14:46:39
# @Author  : xyl (416319808@qq.com)
# @Link    : https://github.com/xylong
# @Version : 1.1

from urllib import request
import re
import os
import json
import platform


class TMM(object):
    """淘女郎爬虫"""

    def __init__(self):
        self.root_path = ''  # 存放目录
        self.code = 'gbk'   # 编码格式
        self.url = 'https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8'  # 美人库

        # 个人中心(爱秀)
        self.ai_show_url = 'https://mm.taobao.com/self/aiShow.htm?userId=%s'
        self.album_url = 'https://mm.taobao.com/self/album/open_album_list.htm?_charset=utf-8&user_id%20='  # 相册列表
        self.album_photo_url = 'https://mm.taobao.com/self/album/album_photo_list.htm?user_id=%s&album_id=%s'   # 具体相册

        self.pattern = {'album': r'<h4>.*?album_id=(.*?)&'}

    # 获取淘女郎list
    def get_tstar_list(self):
        '''30个模特的信息'''
        req = request.Request(self.url)

        res = self.visit(req)
        data = json.loads(res)
        if data['status'] == 1:
            return data['data']['searchDOList']

    # 爱秀(个人中心)
    def aiShow(self, userId):
        url = self.ai_show_url % userId
        req = request.Request(url)
        res = self.visit(req)
        print(res)

    # 获取相册列表
    def get_album_ids(self, userId):
        url = self.album_url + str(userId)
        req = request.Request(url)
        res = self.visit(req)
        pattern = self.compile(self.pattern['album'])
        return re.findall(pattern, res)

    # 获取相册照片
    def get_album_photos(self, user_id, album_id):
        url = self.album_photo_url % (user_id, album_id)
        req = request.Request(url)
        res = self.visit(req)
        print(res)

    # 访问url地址
    def visit(self, req):
        '''访问url，返回utf-8页面'''
        with request.urlopen(req) as f:
            if f.status == 200:
                return f.read().decode('gbk').encode('utf-8').decode('utf-8')

    # 创建目录
    def mkdir(self, path):
        '''没有才创建'''
        if not os.path.exists(path):
            os.mkdir(path)

    # 保存模特信息
    def save_profile(self, mm):
        fileName = self.dir + self.delimiter + \
            mm['realName'] + self.delimiter + mm['realName'] + '.txt'
        with open(fileName, 'w') as f:
            f.write(mm['realName'])

    # 保存图片
    def save_imgs(self):
        pass

    # 预编译正则
    def compile(self, pattern=None):
        return re.compile(pattern, re.S)

    # 保存
    def save(self, tstar):
        path = self.dir + self.delimiter + tstar['realName']
        self.mkdir(path)
        self.save_profile(tstar)

    # 获取目录分隔符
    @property
    def delimiter(self):
        if 'Windows' == platform.system():
            return '\\'
        else:
            return '/'

    @property
    def dir(self):
        return self.root_path

    @dir.setter
    def dir(self, dirName):
        '''创建保存的根目录'''
        if isinstance(dirName, str):
            self.mkdir(dirName)
            self.root_path = dirName

    def run(self):
        name = input('enter save directory: \n')
        self.dir = name
        mm = self.get_tstar_list()
        for tstar in mm:
            self.save(tstar)


mm = TMM()
mm.run()
