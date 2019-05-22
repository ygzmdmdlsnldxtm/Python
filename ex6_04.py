'''Python方法没有重载'''
#测试私有属性
class Employee():
    count = 0
    __a = 1
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def __work(self):
        print("好好工作，赚钱娶媳妇")
    @classmethod
    def __work2(cls):
        print("努力工作，赚钱买房子")
        print(Employee.__a)
e = Employee("吴川枫",20)
print(e.name)
print(Employee.count)
print(e._Employee__age)#访问私有实例属性
print(Employee._Employee__a)#访问私有属性
e._Employee__work()#访问私用实例方法
Employee._Employee__work2()#访问私有方法
print(dir(e))
print(id(Employee("吴川枫",20)))
print(id(e))
print(id(Employee))