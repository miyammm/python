#!/usr/bin/env python2.7
#  -*- coding: utf-8 -*-
import urllib
import urllib2
url="http://apis.juhe.cn/cook/query"
#定义请求数据，并且对数据进行赋值
data={}
data['key']='e0aa7a7d8e25b9227a0a286a3cf6d14f'
data['menu']='土豆'
data['rn']='10'
data['pn']='3'
#对请求数据进行编码
data=urllib.urlencode(data)
#讲数据和url进行连接
request=url+'?'+data
#打开请求，获取对象
requestResponse=urllib2.urlopen(request)
#读取服务端返回的数据
ResponseStr=requestResponse.read()
#打印数据
ResponseStr=ResponseStr.decode("unicode_escape")
print(ResponseStr)
