
'''Python组合
“is-a”关系，我们可以使用“继承”，从而实现子类对象拥有的父类的方法和属性。
“is-a”关系指的是类类似这样的关系：狗是动物，dog is animal.狗类就应该继承动物类。
“has-a"关系 我们可以使用“组合”，也能实现一个类拥有另一个类的方法和属性。
“has-a” 关系指的是这样的关系：手机拥有CPU， MobilePhone has a CPU。
'''
#测试is-a关系，使用继承

class CUP():
    def cup(self):
        print("cup对象：",self)
class Screen():
    def screen(self):
        print("screen对象：",self)
class MobilePhone(CUP,Screen):
    pass
m = MobilePhone()
m.screen()
m.cup()
#测试has-a关系 使用组合
class MobilePhone():
    def __init__(self,cup,screen):
        self.cup = cup
        self.screen = screen
class CUP():
    def cup(self):
        print("cup对象：",self)
class Screen():
    def screen(self):
        print("screen对象：",self)
m = MobilePhone(CUP(),Screen())
m.cup.cup()
m.screen.screen()