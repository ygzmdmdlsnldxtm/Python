'''测试super()，代表父类的定义而不是父类的对象'''
class A():
    def say(self):
        print("A:",self)
    def print_self(self):
        print("这是A类的定义print_self方法：",self)
class B(A):
    def say(self):
        super().say()#继承了父类A的定义，然后我们利用super().调用A父类的定义方法
        print("B:",self)
        super().print_self()
b = B()
b.say()