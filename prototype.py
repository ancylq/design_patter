#!/usr/bin/env python
#coding:utf-8
'''
原型模式
模式特点：用原型实例制定创建对象的种类，并且通过拷贝这些原型创建新的对象。
程序实例：从简历模板生成新的简历
代码特点：简历类Resume提供的clone()方法并不是真正的clone， 只是为已存在对象增加一
        次引用。
python为对象提供的copy模块中的copy方法和deepcopy方法已经实现了原型模式，但由于例
子的层次较浅，二者看不出区别。
'''
import copy

class WorkExp(object):
    place = ''
    year = 0
    
class Resume(object):
    name = ''
    age = 0
    
    def __init__(self, n):
        self.name = n
    
    def set_age(self, a):
        self.age = a
    
    def set_work_exp(self, p, y):
        self.place = p
        self.year = y
        
    def display(self):
        print self.age
        print self.place
        print self.year
        
    def clone(self):
        # 实际不是‘克隆’，只是返回了自己
        return self
    
if __name__ == '__main__':
    a = Resume('a')
    b = a.clone()
    c = copy.copy(a)
    d = copy.deepcopy(a)
    
    a.set_age(7)
    b.set_age(12)
    c.set_age(15)
    d.set_age(18)
    
    a.set_work_exp('PrimarySchool', 1996)
    b.set_work_exp('MidSchool', 2001)
    c.set_work_exp('HighSchool', 2004)
    d.set_work_exp('UniversitySchool', 2007)
    
    a.display()
    b.display()
    c.display()
    d.display()