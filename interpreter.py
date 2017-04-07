#!/usr/bin/env python
#coding:utf-8
'''
解释器模式
模式特点：给定一个语言，定义它的文法的一种表示，并定义一个解释器，这个解释器使用该表
        示来解释语言中的句子。
程序实例：将一段音乐文本翻译成音符。
代码特点：无。

正则表达式就是解释器模式的一种应用。

当有一个语言需要解释执行，并且你可以将语言中的句子表示为一个抽象语法树时，可使用解释器模式。

优点：解释器模式可以很容异地改变和扩展文法，因为该模式使用类来表示文法规则，你可使用
     继承来改变或扩展该文法。也不叫容易实现文法，因为定义抽象语法树中各个节点的类的
     实现大体类似，这些类都易于直接编写。
不足：解释器模式为文法中的每一条规则至少定义了一个类，因此包含许多规则的文法可能难以
     管理和维护。建议当文法非常复杂时，使用其他的技术如语法分析程序或编译器生成器来
     处理。
'''
class PlayContext(object):
    ''' context
    在实例化后，要设置playtext和text属性'''
    pass

class Expression(object):
    '''AbstractExpression'''
    def interpret(self, context):
        if len(context.play_text) == 0:
            return
        else:
            try:
                key, value, context.play_text = context.play_text.split(' ', 2)
            except:
                pass
            self.excute(key, value)
            
    def excute(self, key, value):
        pass
    
class Note(Expression):
    '''音符类(TerminalExpression)'''
    NOTE = {'C':'1', 'D':'2', 'E':'3', 'F':'4', 'G':'5', 'A':'6', 'B':'7'}
    def excute(self, key, value):
        print self.NOTE[key]
        
class Scale(Expression):
    '''音节类 (TerminalExpression)'''
    SCALE = {'1': '低音', '2': '中音', '3': '高音'}
    def excute(self, key, value):
        print self.SCALE[value]
    
class StrErrorException(Exception):
    def __init__(self, raw_str):
        self.message = 'need [O|C|D|E|F|G|A|B], but [%s] was found' % raw_str

if __name__ == '__main__':
    context = PlayContext()
    print '上海滩'
    context.play_text = 'O 2 E 0.5 G 0.5 A 3 E 0.5 G 0.5 D 3 E 0.5 G 0.5 A 0.5'
    try:
        while len(context.play_text) > 0:
            str = context.play_text[0]
            if str == 'O':
                expression = Scale()
            elif str in ['C', 'D', 'E', 'F', 'G', 'A', 'B']:
                expression = Note()
            else:
                raise StrErrorException(str)
            expression.interpret(context)
    except StrErrorException, e:
        print e.message
    except Exception, e:
        print e