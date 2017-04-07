#!/usr/bin/env python
#coding:utf-8
'''
工厂模式
模式特点：定义一个用于创建对象的接口，让子类决定实例化哪一个类。工厂方法使一个类的
        实例化延迟到其子类。
程序实例：基类雷锋类，派生出学生类和志愿者类，由这两种子类完成“学雷锋”工作。子类的创
        建由雷锋工厂的对应的子类完成
代码特点：客户端决定实例化哪一个工厂来实现子类。
'''
class LeiFeng(object):
    def sweep(self):
        '''扫地'''
        print 'LeiFeng sweep'

class Student(LeiFeng):
    def sweep(self):
        print 'Student sweep'

class Volenter(LeiFeng):
    def sweep(self):
        print 'Volenter sweep'


class LeiFengFactory(object):
    def create_leifeng(self):
        temp = LeiFeng()
        return temp
        
class StudentFactory(LeiFengFactory):
    def create_leifeng(self):
        temp = Student()
        return temp

class VolenterFactory(LeiFengFactory):
    def create_leifeng(self):
        temp = Volenter()
        return temp
    
if __name__ == '__main__':
    sf = StudentFactory()
    s = sf.create_leifeng()
    s.sweep()
    
    sdf = VolenterFactory()
    sd = sdf.create_leifeng()
    sd.sweep()
    
'''
如果用简单工厂模式实现，则调用一个新增加的行为，就要重新实例化一个对象
'''