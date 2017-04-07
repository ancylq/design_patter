#!/usr/bin/env python
#coding:utf-8
'''
中介者模式
模式特点：用一个中介对象来封装一系列的对象交互。中介者使各对象不需要显式地相互引用，
        从而使其耦合松散，而且可以独立地改变它们之间的交互。
程序实例：两个对象通过中介者相互通信。
代码特点：Mediatior的出现减少了各个Colleague的耦合，使得可以独立地改变和复用各个
        Colleague类和Mediator。
中介者模式一般应用与一组对象以定义良好但复杂的方式进行通信的场合，以及想定制一个分布
在多个类中的行为，而又不想生成太多的子类的场合。
'''
class Mediator(object):
    '''抽象中介者类'''
    def send(self, message, colleague):
        '''定义一个抽象的发送消息方法，得到同事对象和发送信息'''
        pass
    
class Colleague(object):
    '''抽象同事类'''
    def __init__(self, mediator):
        '''构造方法，得到中介者对象'''
        self.mediator = mediator

class ConcreteMediator(Mediator):
    def send(self, message, colleague):
        '''重写发送信息的方法，根据对象做出选择判断，通知对象'''
        if colleague == self.colleague1:
            self.colleague2.notify(message)
        else:
            self.colleague1.notify(message)
            
class ConcreteColleague1(Colleague):
    def send(self, message):
        self.mediator.send(message, self)
        
    def notify(self, message):
        print '同事1得到信息：', message
        
class ConcreteColleague2(Colleague):
    def send(self, message):
        '''发送信息时通常是中介者发送出去的'''
        self.mediator.send(message, self)
        
    def notify(self, message):
        print '同事2得到信息：', message
        
if __name__ == '__main__':
    m = ConcreteMediator()
    
    # 让两个具体同事类认识中介者对象
    c1 = ConcreteColleague1(m)
    c2 = ConcreteColleague2(m)
    
    # 让中介者认识各个具体同事类对象
    m.colleague1 = c1
    m.colleague2 = c2
    
    # 具体同事类对象的发送信息都是通过中介者转发
    c1.send('吃过饭了吗？')
    c2.send('没有呢，你打算请客？')