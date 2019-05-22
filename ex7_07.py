'''运算符的重载和特殊方法'''
#Python中一切皆对象包括‘+’，‘-’....运算符
class Person():
    def __init__(self,name):
        self.name = name
    def __add__(self, other):
        if isinstance(other,Person):
            return "{0}&&{1}".format(other.name,self.name)
        else:
            return "不是同一个类不可以相加....."

class Animal():
    def __init__(self,name):
        self.name = name
    def __add__(self, other):
        if isinstance(other,Animal):
            return "{0}&&{1}".format(other.name,self.name)
        else:
            return "不是同一个类不可以相加....."
man = Person("吴川枫")
man1 = Person("吴镇东")
cat = Animal("汤姆")
x = cat + man
y = man + man1
print(y)
print(x)