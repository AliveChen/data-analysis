# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random

class GetproxySpiderMiddleware(object):
    proxyList = ['27.204.25.101:80','115.200.160.84:80','117.78.37.198:8000']
    
    def process_request(self, request, spider):
        # Set the location of the proxy
        pro_adr = random.choice(self.proxyList)
        print "USE PROXY -> "+pro_adr
        request.meta['proxy'] = "http://"+ pro_adr
        
'''这里用的免费代理,不用用户名密码的.如果有用户名和密码,还要加入以下代码
proxy_user_pass = "USERNAME:PASSWORD"
encoded_user_pass = base64.encodestring(proxy_user_pass)
request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass'''
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.


