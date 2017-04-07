#!/usr/bin/env python
#coding:utf-8
'''
单例模式
模式特点：保证一个类仅有一个实例，并提供一个访问它的全局访问点。
程序实例：公司人员的组织结构
代码特点：无
我要问的是，python真的需要单例模式吗？我指像其他编程语言中的单例模式。
答案是：不需要！
因为python有模块（module），最pythonic的单例典范。
模块在一个应用程序中只有一份，它本身就是单例的，将你所需要的树形和方法，直接暴露在模
块中变成模块的全局变量和方法即可！
'''
print '---------- 方法1 ----------'
# 重构__new__方法
# 并将一个类的实例绑定到类变量_instance上
# 如果cls._instance为None，说明该类还没有被实例化，实例化该类，返回
# 如果cls._instance不为None，直接返回cls._instance
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            org = super(Singleton, cls)
            cls._instance = org.__new__(cls,*args, **kw)
        return cls._instance
    
class MyClass(Singleton):
    a = 1

one = MyClass()
two = MyClass()

two.a = 3
print one.a    #3
# one 和 two 完全相同，可以用id()，==，is检查，结果全为True

print '---------- 方法2 ----------'
#共享属性;所谓单例就是所有引用(实例、对象)拥有相同的状态(属性)和行为(方法)
#同一个类的所有实例天然拥有相同的行为(方法),
#只需要保证同一个类的所有实例具有相同的状态(属性)即可
#所有实例共享属性的最简单最直接的方法就是__dict__属性指向(引用)同一个字典(dict)
#可参看:http://code.activestate.com/recipes/66531/
class Singleton2(object):
    _state = {}
    def __new__(cls, * args, **kw):
        ob = super(Singleton2, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return obj

class MyClass2(Singleton2):
    a = 2

one = MyClass2()
two = MyClass2()

two.a = 3
print one.a # 3
# one 和 two 是两个不同的对象，id, ==, is的结果都是fals
# 但是one和two具有相同的__dict__属性
id(one.__dict__) == id(two.__dict__)

print '---------- 方法3 ----------'
# 方法1的升级版本
# 使用__metaclass__（元类）的高级python用法
class Singleton3(object):
    def __init__(cls, name, bases, dict):
        super(Singleton3, cls).__init__(name, bases, dict)
        cls._instance = None
        
    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(Singleton3, cls).__call__(*args, **kw)
        return cls._instance

class MyClass3(object):
    __metaclass__ = Singleton3
    
one = MyClass3()
two = MyClass3()
# one 和 two 完全相同，可以用id()，==，is检查，结果全为True

print '---------- 方法4 ----------'
# 方法1更高级的版本
# 使用装饰器（decorator）
# 更pythonic，更elegant的方法
# 单例本身根本不知道自己是单例的，因为它本身（自己的代码）并不是单例的
def singleton(cls): # 若调用时为@singleton(xxx)，则这里改为singleton(cls， *args, **kw)
    instances = {}
    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

@singleton
class MyClass4(object):
    a = 1
    def __init__(self, x=0):
        self.x = x

one = MyClass4()
two = MyClass4()
# one 和 two 完全相同，可以用id()，==，is检查，结果全为True