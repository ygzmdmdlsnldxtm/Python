
'''特殊属性
obj.__dict__ 对象的属性字典
obj.__class__ 对象所属的类
class.__bases__ 类的基类元组(多继承)
class.__base__ 类的基类(单继承)
class.__mro__类层次结构
class.__subclasses__() 子类列表
'''
'''对象的浅拷贝和深拷贝
浅拷贝：
Python 的拷贝一般都是浅拷贝。拷贝时，对象包含的子对象内容不拷贝，因此，源对象和拷贝对象
会引用同一个子对象
深拷贝：
使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象
也不同(地址不同)
'''
import copy
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
#测试浅拷贝
c1 = CUP()
s1 = Screen()
m1 = MobilePhone(c1,s1)
m2 = copy.copy(m1)
print("测试浅拷贝..........")
print(m1,m1.cup,m1.screen)
print(m2,m2.cup,m2.screen)
#测试深拷贝 有点类似与组合的关系
print("测试深度拷贝.........")
m3 = copy.deepcopy(m1)
print(m1,m1.cup,m1.screen)
print(m3,m3.cup,m3.screen)