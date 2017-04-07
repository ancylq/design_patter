#!/usr/bin/env python
#coding:utf-8
'''
适配器模式
模式特点：将一个类的接口转换成客户希望的另外一个接口，使得原本由于接口不兼容而不能一
        起工作的那些类可以一起工作。
程序实例：不会说外语的球员通过翻译与教练和其他球员沟通。
代码特点：用户通过适配器使用一个类的方法。
'''
class Target(object):
    def request(self):
        print 'common request'
        
class Adaptee(object):
    def specific_request(self):
        print 'specific request'
        
class Adapter(Target):
    def  __init__(self, ada):
        self.adaptee = ada
    
    def request(self):
        self.adaptee.specific_request()

if __name__ == '__main__':
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    adapter.request()