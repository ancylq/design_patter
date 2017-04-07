#!/usr/bin/env python
#coding:utf-8
'''
访问者模式
模式特点：表示一个作用于某对象结构中的各元素的操作。它使你可以在不改变各元素的类的前
        提下定义作用于这些元素的新操作。
程序实例：对于男人和女人（接受访问者的元素，ObjectStructure用于穷举这些元素），不
        同的遭遇（具体的访问者）引发两种对象的不同行为。
代码特点：二次分派。
前提：数据结构相对稳定的系统。即objectStructure分类相对较少的情况。

'''
class Action(object):
    '''visitor'''
    def get_man_conclusion(self, man):
        pass
    
    def get_woman_conclusion(self, woman):
        pass
    
class Success(Action):
    '''ConcreteVisitor'''
    def get_man_conclusion(self, man):
        print '%s成功时，背后多半有一个伟大的女人' % man.type
        
    def get_woman_conclusion(self, woman):
        print '%s成功时，背后多半有一个不成功的男人' % woman.type
        
class Failing(Action):
    '''ConcreteVisitor'''
    def get_man_conclusion(self, man):
        print '%s失败时，背后多半有一个伟大的女人' % man.type
        
    def get_woman_conclusion(self, woman):
        print '%s失败时，背后多半有一个不成功的男人' % woman.type
        

class Amativeness(Action):
    '''ConcreteVisitor'''
    def get_man_conclusion(self, man):
        print '%s恋爱时，背后多半有一个伟大的女人' % man.type
        
    def get_woman_conclusion(self, woman):
        print '%s恋爱时，背后多半有一个不成功的男人' % woman.type
        

class Person(object):
    '''Element'''
    def accept(self, action):
        pass
    
class Man(Person):
    '''ConcreteElementA'''
    def __init__(self):
        self.type = '男人'
        
    def accept(self, visitor):
        '''首先在客户程序中将具体状态作为参数传递给‘男人’类完成一次分派，然后‘男人’
        类调用作为参数的‘具体状态’中的方法‘男人反应’，同时将自己（self）作为参数传
        递进去。这便完成了第二次分派'''
        visitor.get_man_conclusion(self) 
        
class Woman(Person):
    '''ConcreteElementB'''
    def __init__(self):
        self.type = '男人'
        
    def accept(self, visitor):
        visitor.get_woman_conclusion(self)
        
class ObjectStructure(object):
    def __init__(self):
        self.elements = []
        
    def attach(self, element):
        '''增加'''
        self.elements.append(element)
        
    def detach(self, element):
        '''删除'''
        self.elements.remove(element)
        
    def display(self, visitor):
        '''显示'''
        for e in self.elements:
            e.accept(visitor)

if __name__ == '__main__':
    o = ObjectStructure()
    
    # 在对象结构中加入要对比的‘男人’和‘女人’
    o.attach(Man())
    o.attach(Woman())
    
    # 查看在各种状态下，’男人‘和’女人‘的反应
    v1 = Success()
    o.display(v1)
    
    v2 = Failing()
    o.display(v2)
    
    v3 = Amativeness()
    o.display(v3)
