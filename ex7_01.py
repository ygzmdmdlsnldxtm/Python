
#测试@property装饰器 将方法调用变成属性调用
class Employee():
    @property
    def salary(self):
        print("salary run......")
        return 10000

emp1 = Employee()
print(emp1.salary)
#property装饰器最简化使用。相当于JAVA中的get set方法
class Employee:
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary
    @property
    def salary(self):
        return self.__salary
    @ salary.setter
    def salary(self,salary):
        if 1000<salary<50000:
            self.__salary = salary
        else:
            print("薪水正常范围是1000-50000")
emp1 = Employee("吴川枫",10000)
emp1.salary = 25000
print(emp1.salary)