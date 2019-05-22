'''测试继承的基本使用,以及重写,可以用super()方法简化过程'''
class Person():
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def say_self(self):
        print("My name is {0} and I'm {1} years old......".format(self.__name,self.__age))

class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score = score
    def say_self(self):
        print("报告老师 我的名字是{0} 我今年{1}岁了 这次考试我得了{2}分......".format(self._Person__name,self._Person__age,self.score))
stu = Student("吴川枫",20,99)
print(Student.mro())
print(stu._Person__age)
stu.say_self()