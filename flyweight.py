#!/usr/bin/env python
#coding:utf-8
'''
享元模式
模式特点：运用共享技术有效地支持大量细粒度的对象。
程序实例：一个网站工厂，根据用户请求的类别返回相应类别的网站。如果这种类别的网站已经
        在服务器上，那么返回这种网站并加上不同用户的独特的数据；如果没有，那么生成
        一个。
代码特点：为了展示每种网站的由用户请求的次数，这里为它们建立了一个引用次数的字典。

在享元对象内部并且不会随环境改变而改变的共享部分，可以成为是享元对象的内部状态。
而随环境改变而改变的，不可以共享的状态就是外部状态。

享元模式可以避免大量非常相似类的开销。在程序设计中，有时需要生成大量细粒度的类实例来
表示数据。如果能发现这些实例除了几个参数外基本上都是相同的，有时就能够大幅度地减少需
要实例化的类的数量。如果能把那些参数移到类实例的外面，在方法调用时将它们传递过来，就
可以通过共享大幅度地减少单个实例的数目。

如果一个应用程序使用了大量的对象，而大量的对象造成了很大的存储开销时就应该考虑用；
还有就是对象的大多数状态可以外部状态，如果删除对象的外部状态，那么可以用相对较少的共
享对象取代很多对象，此时可以考虑使用享元模式。
使用享元模式需要维护一个记录了系统已有的所有享元列表，而者本身需要耗费资源，另外享元
模式使得系统更加复杂。为了使对象可以共享，需要将一些状态外部化，这使得程序的逻辑复杂
化。因此，应当在有足够多的对象实例可供共享时才值得使用享元模式。

'''
class User(object):
    '''外部代码'''
    def __init__(self, name):
        self.name = name
        
class WebSite(object):
    def user(self, user):    # user可写可不写，重构时要传
        pass
    
class ConcreteWebSite(WebSite):
    def __init__(self, web_name):
        self.web_name = web_name
        
    def use(self, user):
        print '网站分类：' + self.web_name + ' 用户：' + user.name
        
class WebSiteFactory(object):
    def __init__(self):
        self.flyweights = {}
        
    def get_website_category(self, type):
        if type not in self.flyweights:
            self.flyweights[type] = ConcreteWebSite(type)
        return self.flyweights[type]
    
    def get_website_count(self):
        return len(self.flyweights)

if __name__ == '__main__':
    f = WebSiteFactory()
    
    fa = f.get_website_category('产品展示')
    fa.use(User('小菜'))
    
    fb = f.get_website_category('产品展示')
    fb.use(User('大鸟'))
    
    fc = f.get_website_category('产品展示')
    fc.use(User('娇娇'))
    
    fd = f.get_website_category('博客')
    fd.use(User('老顽童'))
    
    fe = f.get_website_category('博客')
    fe.use(User('桃谷六仙'))
    
    print '得到网站分类总数为：', f.get_website_count()
    
'''
>>> a = 'a'
>>> b = 'a'
>>> id(a)
140265555973664
>>> id(b)
140265555973664
>>> class Test(object):
...     pass
... 
>>> c = Test()
>>> d = Test()
>>> id(c)
140265554981328
>>> id(d)
140265554981264
>>> e = 1
>>> f = 1
>>> id(e)
24711512
>>> id(f)
24711512
>>> g=[]
>>> h=[]
>>> id(g)
140265554937904
>>> id(h)
140265554858928

python中字符串和数字类型的创建，使用的就是享元模式
'''