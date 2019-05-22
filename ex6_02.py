
'''Python OOP'''
'''当函数进行到class类是在堆里会出现一个模板'''
class Student():
    pass
print(type(Student))
#属性和实例属性定义在特殊的方法里即构造方法里面__init__()
class Student():
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def say_self(self):
        print("My name is {}".format(self.name))
    def say_score(self):
        print("My score is {}".format(self.score))
        self.say_self()
stu = Student("吴镇东",90)#实例化过程实际上调用了两个方法一个new()方法创建一个空对象只有地址再调用__init__()方法赋值
stu1 = Student("吴川枫",100)
#stu.say_score()
stu.age = 30
stu.salary = 3000
print(stu.__dict__)
print(stu1.__dict__)
print(dir(stu))
print(dir(stu1))
dir()#可以获得对象的所有属性,方法
#obj.__dict__获得对象属性的字典
#实例属性
n = int(input("请输入："))
for i in range(1,n+1):
    for j in range(0,n-i):
        print(end=" ")
    for k in range(n-i,n):
        print("*",end=" " )
    print()
#类属性调用类名.属性名
class Student():
    count = 0
    teacher = "Mark"
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        Student.count += 1
    def say_hello(self):
        print("{} 老师，早上好！ ".format(Student.teacher))
        self.say_self()
    def say_self(self):
        print("My name is {0} and I'm from {1}".format(self.name,self.grade))
    @classmethod
    def f(cls):
        print(cls.count)
stu1 = Student("吴川枫","高三一班")
stu2 = Student("吴镇东","高三二班")
stu1.say_hello()
stu2.say_hello()
print("一共创建了{}个对象".format(Student.count))
Student.f()