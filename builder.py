#!/usr/bin/env python
#coding:utf-8
'''
建造者模式
模式特点：讲一个复杂对象的构建（Director）与它的表示（Builder）分离，使得同样的构
        建过程可以创建不同的表示（ConcreteBuilder）。
程序实例：“画”出一个四肢健全（头身手脚）的小人。
代码特点：无
建造者模式是在当创建复杂对象的算法应该独立于该对象的组成部分以及他们的装配方式时适用的模式
'''
class Person(object):
    def create_head(self):
        pass
    
    def create_hand(self):
        pass
    
    def create_body(self):
        pass
    
    def create_foot(self):
        pass
    
class ThinPerson(Person):
    def create_head(self):
        print 'draw thin head'
    
    def create_hand(self):
        print 'draw thin hand'
        
    def create_body(self):
        print 'draw thin body'
        
    def create_foot(self):
        print 'draw thin foot'
        
class FatPerson(Person):
    def create_head(self):
        print 'draw fat head'
    
    def create_hand(self):
        print 'draw fat hand'
        
    def create_body(self):
        print 'draw fat body'
        
    def create_foot(self):
        print 'draw fat foot'
        
class Director(object):
    def __init__(self, temp):
        self.p = temp
        
    def create(self):
        self.p.create_head()
        self.p.create_body()
        self.p.create_hand()
        self.p.create_foot()
        
if __name__ == '__main__':
    p = FatPerson()
    d = Director(p)
    d.create()