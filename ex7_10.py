
'''Python OOP练习
工厂模式
单例模式
'''
class CarFactory():
    __obj = None
    __init_flag = True
    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(CarFactory)
        return cls.__obj
    def __init__(self):
        if CarFactory.__init_flag :
            print("CarFactory init.....")
            CarFactory.__init_flag = False
    def creat_car(self,brand):
        if brand == "宝马":
            return BMW()
        elif brand == "比亚迪":
            return BYD()
        elif brand == "奔驰":
            return Benz()
        else:
            print("我们还没有这个品牌.....抱歉")

class Benz():
    def __init__(self):
        print("我们正在为您制造你要的车子.....")
class BMW():
    def __init__(self):
        print("我们正在为您选购你需要车子的配件.......")
class BYD():
    def __init__(self):
        print("我们正在为您开发票......")
factory = CarFactory()
client1 = factory.creat_car("比亚迪")
client2 = factory.creat_car("凯迪拉克")
factory1 = CarFactory()
client3 = factory1.creat_car("比亚迪")
print(factory1 is factory)
print(id(client1))
print(id(client2))
print(id(client3))
print(id(factory))
print(id(factory1))
'''总结定义一个类如果直接写print()方法那么无new不new 一个新对象都会执行print()语句
因为当执行这个class的时候会在堆里创建一个这个类的模板，然后这个print语句自动执行
但是我们可以将print语句定义在__init__()构造方法里这样只有new完对象的时候在执行__init__()方法里的print语句
简而言之就是如果不new对象就不会执行print语句
'''
'''单例模式核心作用确保一个类只有一个实例，并且提供一个访问实例的全局访问点'''
#测试单例模式 重写new方法和构造方法

class MySingleton():
    __obj = None
    __init_flag = True
    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)
        return cls.__obj

    def __init__(self):
       if MySingleton.__init_flag:
           print("init......")
           MySingleton.__init_flag = False

a = MySingleton()
b = MySingleton()
print(a is b)
'''总结单例模式  将目标类单例对象保存在其属性中
    只创建一个实例
'''