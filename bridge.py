#!/usr/bin/env python
#coding:utf-8
'''
桥接模式
模式特点：将抽象部分与它的现实部分分离，使它们都可以独立地变化。
程序实例：两种品牌的手机，要求它们都可以运行游戏和通讯录两个软件，而不是为每个品牌的
        手机都编写不同的软件。
代码特点：无。
'''
class HandSetSoft(object):
    def run(self):
        pass
    
class HandSetGame(HandSetSoft):
    def run(self):
        print 'Game'
        
class HandSetAddr(HandSetSoft):
    def run(self):
        print 'Address list'
        
class HandSetBrand(object):
    def __init__(self):
        self.m_soft = None
        
    def set_hand_soft(self, temp):
        self.m_soft = temp
        
    def run(self):
        pass
    
class HandSetBrandM(HandSetBrand):
    def run(self):
        if self.m_soft:
            print 'BrandM'
            self.m_soft.run()
            
class HandSetBrandN(HandSetBrand):
    def run(self):
        if self.m_soft:
            print 'BrandN'
            self.m_soft.run()
            
if __name__ == '__main__':
    brand_m = HandSetBrandM()
    brand_m.set_hand_soft(HandSetAddr())
    brand_m.run()
    
    brand_n = HandSetBrandN()
    brand_n.set_hand_soft(HandSetAddr())
    brand_n.run()
    brand_n.set_hand_soft(HandSetGame())
    brand_n.run()