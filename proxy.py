#!/usr/bin/env python
#coding:utf-8
'''
代理模式
模式特点：为其他对象提供一种代理以控制对这个对象的访问。
程序实例：A代替B送花给C
代码特点：无
'''
class Subject(object):
    '''
    定义了RealSubject和Proxy的公用接口，这样就在任何使用RealSubject的地方都可以
    使用Prosy
    '''
    def request(self):
        return 0
    
class RealSubject(Subject):
    def request(self):
        print 'Real Request'

class Proxy(Subject):
    def request(self):
        self.real = RealSubject()
        self.real.request()
        
if __name__ == '__main__':
    p = Proxy()
    p.request()
