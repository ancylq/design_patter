#!/usr/bin/env python
#coding:utf-8
'''
组合模式
模式特点：将对象组合成树形结构以表示‘部分-整体’的层次结构。组合模式使得用户对单个对象
        和组合对象的使用具有一致性。
程序实例：公司人员的组织结构
代码特点：Originator根据保存的Memento信息还原到前一状态。
需求中是体现部分与整体层次的结构时，希望用户可以忽略组合对象与单个对象的不同，统一使
用组合结构中的所有对象时，就应该考虑使用组合模式了。
'''
class Component(object):
    def __init__(self, strName):
        self.m_name = strName
        
    def add(self, com):
        pass
    
    def remove(self, com):
        pass
    
    def display(self, depth):
        pass
    
class Leaf(Component):
    def add(self, com):
        print "leaf can't add"
        
    def remove(self, com):
        print "leaf can't remove"
        
    def display(self, depth):
        strtemp = ''
        for i in range(depth):
            strtemp += '-'
        strtemp += self.m_name
        print strtemp
        
class Composite(Component):
    def __init__(self, strName):
        self.m_name = strName
        self.c = []
        
    def add(self, com):
        self.c.append(com)
        
    def remove(self, com):
        if com in self.c:
            self.c.remove(com)
            
    def display(self, depth):
        strtemp = ''
        for i in range(depth):
            strtemp += '-'
        strtemp += self.m_name
        print strtemp
        for com in self.c:
            com.display(depth+2)
        
if __name__ == '__main__':
    p = Composite('总部')
    p.add(Leaf('人事部'))
    p.add(Leaf('事业部'))
    
    p1 = Composite('华东分部')
    p1.add(Leaf('人事部'))
    p1.add(Leaf('技术部'))
    
    p.add(p1)
    p.display(1)
'''
透明方式：在Component中声明所有用来管理子对象的方法，其中包括add、remove等。这样实
        现Component接口的所有子类都具备了add和remove。这样做的好处就是叶节点和枝
        节点对于外界没有区别，它们具备完全一致的行为接口。但问题也很明显，因为Leaf类
        本身不具备add（）、remove（）方法的功能，所以实现它是没有意义的。
安全方式：在Component接口中不去声明add和remove方法，那么子类的Leaf也就不需要去实
        现它，而是在Composite声明所有用来管理子类对象的方法，这样做就不会出现刚才
        提到的问题，不过由于不够透明，所以树叶和树枝类将不具有相同的接口，客户端的调
        用需要做相应的判断，带来了不便。
'''
