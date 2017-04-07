#!/usr/bin/env python
#coding:utf-8
'''
装饰模式
模式特点：动态地给一个对象添加一些额外的职责。
程序实例：展示一个人一件一件穿衣服的过程。
代码特点：就增加功能来说，装饰模式比生成子类更为灵活。
'''
class Person(object):
    def __init__(self, tname):
        self.name = tname
    
    def show(self):
        print 'dressed %s' % (self.name)

class Finery(Person):
    componet = None
    
    def __init__(self):
        pass
    
    def decorate(self, ct):
        self.componet = ct
        
    def show(self):
        if self.componet != None :
            self.componet.show()
            
class TShirts(Finery):
    def __init__(self):
        pass
    
    def show(self):
        print 'Big T-shirt'
        self.componet.show()
        
class BigTrouser(Finery):
    def __init__(self):
        pass
    
    def show(self):
        print 'Big Trouser'
        self.componet.show()
        
if __name__ == '__main__':
    p = Person('somebody')    # 首先用Person实例化一个对象p
    bt = BigTrouser()
    ts = TShirts()
    bt.decorate(p)            # 然后再用BigTrouser的实例化对象bt来包装p
    ts.decorate(bt)           # 再用TShirts的实例化对象ts来包装bt
    ts.show()                 # 最终执行ts的show()方法
"""
输出：
Big T-shirt
Big Trouser
dressed somebody
"""