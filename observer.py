#!/usr/bin/env python
#coding:utf-8
'''
观察者模式
模式特点：定义了一种一对多的依赖关系，让多个观察者对象同时监听某一个主题对象。这个主题
        对象在状态发生变化时，会通知所有观察者对象，使它们能够自动更新自己。
程序实例：公司里有两种上班时趁老板不在时偷懒的员工：看NBA和看股票行情的，并且事先让老
        板秘书当老板出现时通知他们继续做手头上的工作。
代码特点：无
当一个对象的改变需要同时改变其他对象，而且不知道具体有多少对象有待改变时，应考虑使用观察者模式。
一个抽象模型有两个方面，其中一方面依赖于另一方面，这时使用观察者模式可以将这两者封装
在独立的对象中使它们各自独立地改变和复用。
观察者模式所做的工作其实就是在解除耦合。让耦合双方都依赖于抽象，而不是依赖于具体。
从而使的各自的变化都不会影响另一边的变化。
'''
class Observer(object):
    '''观察者通知被观察者更新工作状态的抽象类，可以拥有多个观察者'''
    def __init__(self, strname, strsub):
        self.name = strname
        self.sub = strsub
        
    def update(self):
        pass
    
class StockObserver(Observer):
    '''股票观察者......'''
    def update(self):
        print '%s:%s, stop watching stock and go on work' % (self.name, self.sub.action)
        
class NBAObserver(Observer):
    '''NBA观察者......'''
    def update(self):
        print '%s:%s, stop watching NBA and go on work' % (self.name, self.sub.action)
        
class SecretaryBase(object):
    def __init__(self):
        self.observers = []
        
    def attach(self, new_observer):
        '''增加要通知的人'''
        pass
    
    def notify(self):
        '''通知要通知的人'''
        pass
    
    def delete(self, observer):
        '''删除要通知的人'''
        pass
    
class Secretary(SecretaryBase):
    def attach(self, new_observer):
        self.observer.append(new_observer)
        
    def notify(self):
        for p in self.observers:
            p.update()
            
    def delete(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
            
if __name__ == '__main__':
    p = Secretary()
    s1 = StockObserver('lq', p)
    s2 = NBAObserver('sxm', p)
    p.attach(s1)
    p.attach(s2)
    p.action = 'WARNING:BOSS'
    p.notify()