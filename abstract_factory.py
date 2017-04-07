#!/usr/bin/env python
#coding:utf-8
'''
抽象工厂模式
模式特点：提供一个创建一系列相关或相互依赖对象的接口，而无需知道能够它们具体的类。
程序实例：提供对不同的数据库访问的支持。
代码特点：无
注：'I'开头的类是接口，需要子类去实现，此命名方法为C#风格，python无要求。
'''
class IUser(object):
    def get_user(self):
        pass
    
    def insert_user(self):
        pass
    
class IDepartment(object):
    def get_department(self):
        pass
    
    def insert_department(self):
        pass
    
class CAccessUser(IUser):
    def get_user(self):
        print 'Access database get user information'
        
    def insert_user(self):
        print 'Access database insert user information'
        
class CAccessDepartment(IDepartment):
    def get_department(self):
        print 'Access database get department information'
        
    def insert_department(self):
        print 'Access database insert department information'
        
class CSqlUser(IUser):
    def get_user(self):
        print 'SQL database get user information'
        
    def insert_user(self):
        print 'SQL database insert user information'
        
class CSqlDepartment(IDepartment):
    def get_department(self):
        print 'SQL database get department information'
        
    def insert_department(self):
        print 'SQL database insert department information'
        
class IFactory(object):
    def create_user(self):
        pass
    
    def create_department(self):
        pass
    
class AccessFactory(IFactory):
    def create_user(self):
        temp = CAccessUser()
        return temp
    
    def create_department(self):
        temp = CAccessDepartment()
        return temp
    
class SqlFactory(IFactory):
    def create_user(self):
        temp = CSqlUser()
        return temp
    
    def create_department(self):
        temp = CSqlDepartment()
        return temp
    
if __name__ == '__main__':
    factory = SqlFactory() # 如果要换成access数据库，则只需要更改这行为AccessFactory即可
    user = factory.create_user()
    depart = factory.create_department()
    user.get_user()
    depart.get_department()
