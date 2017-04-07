#!/usr/bin/env python
#coding:utf-8
'''
备忘录模式
模式特点：在不破坏封装性的前提下，捕获一个对象的内部专题，并在该对象之外保存这个状态。
        这样以后就可以将该对象回复到原先保存的状态。
程序实例：玩游戏在打boss前保存当前状态，等损失惨重时，可回到保存的状态。要备份的状态
        越多越占内存。
代码特点：Originator根据保存的Memento信息还原到前一状态。
'''
class Originator(object):
    def __init__(self):
        self.state = ''
        
    def show(self):
        print self.state
    
    def create_memo(self):
        return Memo(self.state)
    
    def set_memo(self, memo):
        self.state = memo.state
        
class Memo(object):
    state = ''
    def __init__(self, ts):
        self.state = ts
        
class Caretaker(object):
    memo = ''
    
if __name__ == '__main__':
    on = Originator()
    on.state = 'on'
    on.show()
    c = Caretaker()
    c.memo = on.create_memo()
    on.state = 'off'
    on.show()
    on.set_memo(c.memo)
    on.show()