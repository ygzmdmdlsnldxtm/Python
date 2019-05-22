"""
__del__方法(析构函数)和垃圾回收机制
"""
class Test():
    def say_hello(self):
        print("hello")
    def __del__(self):
        print("对象被销毁{0}".format(self))
person1 = Test()
person2 = Test()
person3 = Test()
del person2
print("程序结束......")