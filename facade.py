#!/usr/bin/env python
#coding:utf-8
'''
外观模式
模式特点：为子系统中的一组接口提供一个一致的界面。
程序实例：接口将几种调用分别组合成两组，用户通过接口调用其中的一组。
代码特点：此模式定义了一个高层接口，这个接口使得这一子系统更加容易使用。
'''
class SubSystemOne(object):
    def method_one(self):
        print 'SubSystemOne'
        
class SubSystemTwo(object):
    def method_two(self):
        print 'SubSystemTwo'
        
class SubSystemThree(object):
    def method_three(self):
        print 'SubSystemThree'
        
class SubSystemFour(object):
    def method_four(self):
        print 'SubSystemFour'

class Facade(object):
    def __init__(self):
        self.one = SubSystemOne()
        self.two = SubSystemTwo()
        self.three = SubSystemThree()
        self.four = SubSystemFour()
        
    def method_a(self):
        print 'method_a'
        self.one.method_one()
        self.two.method_two()
        self.four.method_four()
        
    def method_b(self):
        print 'method_b'
        self.one.method_one()
        self.four.method_four()
        
if __name__ == '__main__':
    facade = Facade()
    facade.method_a()
    facade.method_b()