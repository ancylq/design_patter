#!/usr/bin/env python
#coding:utf-8
'''
命令模式
模式特点：将一个请求封装为一个对象，从而使你可用不同的请求对客户进行参数化；对请求排
        队或记录请求日志，以及支持可撤销的操作。
程序实例：烧烤店有两种食物，羊肉串和鸡翅。客户向服务员点单，服务员将点好的单告诉大厨，
        由大厨进行烹饪。可以进行点单、增加烤串和撤销。
代码特点：无。
注：在遍历时不要用remove，会出现bug。因为remove打乱了for迭代查询列表的顺序。
'''
class Barbecue(object):
    def make_mutton(self):
        '''烤羊肉串'''
        print '烤羊肉串'
        
    def make_chickenwing(self):
        '''烤鸡翅'''
        print '烤鸡翅'
        
class Command(object):
    def __init__(self, temp):
        self.receiver = temp
        
    def execute_cmd(self):
        pass
    
class MakeMuttonCmd(Command):
    def execute_cmd(self):
        self.receiver.make_mutton()
        
class ChickenWingCmd(Command):
    def execute_cmd(self):
        self.receiver.make_chickenwing()
        
class Waiter(object):
    def __init__(self):
        self.order = []
        
    def set_cmd(self, command):
        '''下单'''
        self.order.append(command)
        print '增加一道菜'
        
    def del_cmd(self, command):
        '''撤销已定的菜'''
        if command in self.order:
            self.order.remove(command)
            print '撤销点过的菜'
        else:
            print '没点这道菜'
            
    def notify(self):
        '''通知大厨开始做菜'''
        for cmd in self.order:
            cmd.execute_cmd()
            
if __name__ == '__main__':
    barbecue = Barbecue()
    cmd = MakeMuttonCmd(barbecue)
    cmd2 = ChickenWingCmd(barbecue)
    waiter = Waiter()
    waiter.set_cmd(cmd)
    waiter.set_cmd(cmd2)
    waiter.notify()