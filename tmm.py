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


class TMM(object):
    """淘女郎爬虫"""

    def __init__(self):
        pass

    # 获取淘女郎list
    def get_tstar_list(self):
        '''30个模特的信息'''
        req = request.Request(
            'https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8')

        with request.urlopen(req) as f:
            if f.status == 200:
                json_str = f.read().decode('gbk').encode('utf-8')
                data = json.loads(json_str.decode('utf-8'))
                if data['status'] == 1:
                    return data['data']['searchDOList']

    def aiShow(self, userId):
        req = request.Request(
            'https://mm.taobao.com/self/aiShow.htm?userId=%s' % userId)
        with request.urlopen(req) as f:
            page = f.read().decode('gbk')
            print(page)

    # 获取相册列表
    def get_album_list(self, userId):
        req = request.Request('https://mm.taobao.com/self/album/open_album_list.htm?_charset=utf-8&user_id%20=' + str(userId)
            )
        with request.urlopen(req) as f:
            page = f.read().decode('gbk')
            reg = r'class="mm-first" href="//(.*?)"'
            res = re.findall(reg,page)
            for i in res:
                print(i)

    # 获取相册照片
    def get_album_photos(self, user_id, album_id):
        pass

    # 访问url地址
    def visit(self, url):
        with request.urlopen(url) as f:
            if f.status ==200:
                return f.read().decode('gbk')

    def run(self):
        self.get_album_list(646632716)


mm = TMM()
mm.run()
