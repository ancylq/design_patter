#!/usr/bin/env python
#coding:utf-8
'''
策略模式
模式特点：定义一系列的算法，把每个算法封装起来，并且使他们可相互替换。本模式使得算法
        可独立于使用它的客户而变化。也称政策模式（Policy）
程序实例：商场收银软件。需要根据不同的销售策略方式进行收费。
代码特点：不同于简单工厂模式（static_factory_method），这里使用字典时为了避免关
        键字不在字典里导致bug出现。
工厂模式：我没有，我需要你的。策略模式：我自己有，我用我自己的。
'''
class CashSuper(object):
    def AcceptCash(self, money):
        return 0

class CashNormal(CashSuper):
    '''正常收费'''
    def AcceptCash(self, money):
        return money
    
class CashRebate(CashSuper):
    '''打折'''
    discount = 0
    
    def __init__(self, ds):
        self.discount = ds
        
    def AcceptCash(self, money):
        return money * self.discount
    
class CashReturn(CashSuper):
    '''满减活动'''
    total = 0
    ret = 0
    
    def __init__(self, t, r):
        self.total = t
        self.ret = r
        
    def AcceptCash(self, money):
        if money >= self.total:
            return money-self.re
        else:
            return money

class CashContext(object):
    def __init__(self, csuper):
        self.cs = csuper
    
    def getResult(self, money):
        return self.cs.AcceptCash(money)
    
if __name__=='__main__':
    money = input('money:')
    strategy = {}
    strategy[1] = CashContext(CashNormal())
    strategy[2] = CashContext(CashRebate(0.8))
    strategy[3] = CashContext(CashReturn(300, 100))
    ctype = input('type:[1] for normal; [2] for 80% discount; [3] for 300-100.')
    if ctype in strategy:
        cc = strategy[ctype]
    else:
        print 'Undefine type.Use normal mode.'
        cc = strategy[1]
    print 'You will pay:%d'%(cc.getResult(money))