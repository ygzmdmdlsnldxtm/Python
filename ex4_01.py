'''
Python
类，对象
实例属性
实例方法
类方法
类属性
静态方法
'''
class Person():
    count = 0
    school = "SDZYY"
    def creat(self):
        print(self)
        person01 = self.__class__("小米",19)
        person01.say_self()
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.count += 1
    def say_self(self):
        print("My name is {0},I am {1} years old".format(self.name,self.age))
        print("My school is {0}".format(Person.school))
    @classmethod
    def print_school(cls):
        print(cls.school)
    @staticmethod#类方法和静态方法在不能调用实例属性与实例方法
    def add(a,b):
        print("{0}+{1}={2}".format(a,b,a+b))
person = Person("小吴",20)
person02 = Person("小吴",20)
# print(person)
# person.say_self()
# person.creat()
print(Person)
print(type(Person))
print(id(Person))
#print(Person("小吴",20))#Person模块（Type）的地址
print(person)
print(person02)
print("一共创建了{0}".format(Person.count))
Person.print_school()
Person.add(5,5)