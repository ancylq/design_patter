#!/usr/bin/env python
#coding:utf-8
'''
模板方法模式
模式特点：定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。
程序实例：考试时使用同一种考卷（父类），不同学生上交自己的试卷（子类方法实现）。
代码特点：模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。
'''
class TestPaper(object):
    def test_question1(self):
        print '''杨过得到，后来给了郭靖，炼成倚天剑‘屠龙刀的玄铁可能是[]
                 a.球磨铸铁 b.马口铁 c.高速合金钢 d.碳素纤维
              '''
        print '答案是（%s）' % self.answer1()
        
    def test_question2(self):
        print '''杨过、程英、陆无双铲除了情花，造成[]
                 a.使这种植物不再害人 b.使一种珍稀物种灭绝
                 c.破坏了那个生物圈的生态平衡 d.造成该地区沙漠化
              '''
        print '答案是（%s）' % self.answer2()
        
    def answer1(self):
        return ''
    
    def answer2(self):
        return ''
    
    
class TestPaperA(TestPaper):
    def answer1(self):
        return 'a'
    
    def answer2(self):
        return 'c'
    
class TestPaperB(TestPaper):
    def answer1(self):
        return 'b'
    
    def answer2(self):
        return 'a'
    
if __name__ == '__main__':
    s1 = TestPaperA()
    s2 = TestPaperB()
    
    print 'student1'
    s1.test_question1()
    s1.test_question2()
    
    print 'student2'
    s2.test_question1()
    s2.test_question2()