# -*- coding: cp936 -*-
from urllib2 import Request  
import re  
import threading  
import time  
  
class TestProxy(object):  
    def __init__(self):  
        self.sFile=r'proxy'+time.strftime('%Y-%m-%d',time.localtime())+'.txt'  
   #     self.sFile=r'alive.txt'  
        self.dFile=r'alive_.txt'  
        self.URL=r'http://www.baidu.com/'  
        self.threads=10  
        self.timeout=3  
        self.regex=re.compile(r'baidu.com')  
        self.aliveList=[]  
  
        self.run()  
  
    def run(self):  
        with open(self.sFile,'r') as fp:  
            lines=fp.readlines()  
            line=lines.pop()  
            while lines:  
                for i in range(self.threads):  
                    try:  
                        t=threading.Thread(target=self.linkWithProxy,args=(line,))  
                        t.start()  
  
                        if lines:  
                            line=lines.pop()  
                        else:  
                            continue  
                    except:  
                        print('创建线程失败！\n')  
                          
  
        with open(self.dFile,'a') as fp:  
            for i in range(len(self.aliveList)):  
                fp.write(self.aliveList[i])  
  
    def linkWithProxy(self,line):  
        lineList=line.split('\t')  
        protocol=lineList[3].lower()  
        server=protocol+r'://'+lineList[1]+':'+lineList[2]  
        opener=Request.build_opener(Request.ProxyHandler({protocol:server}))  
        request.install_opener(opener)  
        try:  
            response=Request.urlopen(self.URL,timeout=self.timeout)  
        except:  
            print('%s connect failed!\n' %server)  
            return  
        else:  
            try:  
                strRe=response.read()  
            except:  
                print('%s connect failed!\n' %server)  
                return  
            if self.regex.search(str(strRe)):  
                print('%s connect success!！！！！！！\n' %server)  
                self.aliveList.append(line)  
  
if __name__=='__main__':  
    tp=TestProxy()  
