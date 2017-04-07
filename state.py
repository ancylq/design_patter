#!/usr/bin/env python
#coding:utf-8
'''
状态模式
模式特点：当一个对象的内在状态改变时允许改变其行为，这个对象看起来像是改变了其类。
程序实例：主要解决的是当控制一个对象状态转换的条件表达式过于复杂时的情况。把状态的判
        断逻辑转移到表示不同状态的一系列类当中，可以把复杂的判断逻辑简化.
代码特点：无
'''
class State(object):
    def write_program(self):
        pass
    
class NoonState(State):
    def write_program(self, w):
        print 'noon working'
        if w.hour<13:    # 12-13点进入fun状态
            print 'fun'
        else:
            # 13点以后进入最终的状态
            print 'need to rest'
            
class ForenoonState(State):
    def write_program(self,w):
        if w.hour <12 :
            print 'mornint working'
            print 'energetic'
        else:
            # 大于12点，进入下个状态的判断
            w.set_state(NoonState())
            w.write_program()    # 执行Work类的write_program方法

class Work(object):
    def __init__(self):
        self.hour = 9    # 状态初始时间
        self.current = ForenoonState()    # 初始状态要做的工作
    
    def set_state(self, temp):
        self.current = temp
        
    def write_program(self):
        self.current.write_program(self)    # 执行相关状态下的write_program方法
        
if __name__ == '__main__':
    mywork = Work()
    mywork.hour = 8
    mywork.write_program()
    mywork.hour = 14
    mywork.write_program()
'''
若增加6点的状态，则需要将Work的初始化改成6点要做的事，6点的类里时间判断小于6即可
'''