#!/usr/bin/env python
#coding:utf-8
'''
简单工厂模式
模式特点：工厂根据条件产生不同功能的类
程序实例：四则运算计算器。根据用书的输入产生相应的运算类，用这个运算类处理具体的运算
代码特点：switch...case...分支使用字典的方式代替
        使用异常机制对除数为0的情况进行处理
工厂模式：我没有，我需要你的。策略模式：我自己有，我用我自己的。
'''
class Operation(object):
    def getResult(self):
        pass

class OperationAdd(Operation):
    def getResult(self):
        return self.op1+self.op2

class OperationSub(Operation):
    def getResult(self):
        return self.op1-self.op2

class OperationMul(Operation):
    def getResult(self):
        return self.op1*self.op2

class OperationDiv(Operation):
    def getResult(self):
        try:
            result = self.op1/self.op2
            return result
        except Exception as e:
            print e
            return 0

class OperationUndef(Operation):
    def getResult(self):
        print 'Undefine operation.'
        return 0

class OperationFactory(object):
    '''
    工厂类
    '''
    operation = {}
    operation['+'] = OperationAdd()
    operation['-'] = OperationSub()
    operation['*'] = OperationMul()
    operation['/'] = OperationDiv()
    
    def createOperation(self, ch):
        if ch in self.operation:
            op = self.operation[ch]
        else:
            op = OperationUndef()
        return op

if __name__ == '__main__':
    op = raw_input('operator:')
    opa = input('a:')
    opb = input('b:')
    factory = OperationFactory()
    cal = factory.createOperation(op)
    cal.op1 = opa
    cal.op2 = opb
    result = cal.getResult()
    print 'a'+op+'b='+str(result)

"""
简单工厂模式的最大有点在于工厂类中包含了必要的逻辑判断，根据客户端的选择条件动态实例
化相关的类，对于客户端来说，去除了与具体昌平的依赖。但问题也就在这里，若再增加运算，
需修改原有的工厂类，这样一来，不但对扩展开放，也对修改开放，违背了开放-封闭原则！于是
就有了工厂方法。
开放-封闭原则：对扩展开放，对修改封闭。
"""