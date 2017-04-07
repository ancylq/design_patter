#!/usr/bin/env python
#coding:utf-8
'''
职责链模式
模式特点：使多个对象都有机会处理请求，从而避免请求的发送者和接受者之间的耦合关系。将
        这个对象练成一条链，并沿着这条链传递该请求，直到有一个对象处理它为止。
程序实例：请假和加薪等请求发给上级，如果上级无权决定，那么递交给上级的上级。
代码特点：无。
'''
class Request(object):
    def __init__(self, type, name, num):
        self.type = type
        self.num = num
        self.name = name
        
class Manager(object):
    def __init__(self, name):
        self.name = name
        
    def set_successor(self, temp):
        '''设置继承者'''
        self.mamager = temp
        
    def get_result(self, req): # 不写req参数，也不会报错，但不知道与重构的是否一样
        pass
    
class ManagerLow(Manager):
    def get_result(self, req):
        if(req.num>=0 and req.num<10):
            print '%s请求%s%d，%s批准了' % (req.name, req.type, req.num, self.name)
        else:
            self.mamager.get_result(req)
            
class ManagerMiddle(Manager):
    def get_result(self, req):
        if(req.num>=10 and req.num<100):
            print '%s请求%s%d，%s批准了' % (req.name, req.type, req.num, self.name)
        else:
            self.mamager.get_result(req)

class ManagerHight(Manager):
    def get_result(self, req):
        if req.num>=100:
            print '%s请求%s%d，%s批准了' % (req.name, req.type, req.num, self.name)

if __name__ == '__main__':
    manager1 = ManagerLow('Zhang')
    manager2 = ManagerMiddle('Lee')
    manager3 = ManagerHight('Liu')
    
    # 设置上下级
    manager1.set_successor(manager2)
    manager2.set_successor(manager3)
    
    req = Request('加薪', '小菜', 1000)
    manager1.get_result(req)
    
    req1 = Request('休假', '大鸟', 3)
    manager1.get_result(req1)