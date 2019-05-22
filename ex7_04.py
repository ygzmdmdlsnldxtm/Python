'''多重继承'''
class A():
    def aa(self):
        print("aa")
    def say(self):
        print("say AAA!")
class B():
    def bb(self):
        print("bb")
    def say(self):
        print("say BBB!")
class C(B,A):#MRO：方法解析顺序，我们可以通过mro()方法获得“类的层次结构”，方法的顺序也是按这个“类的层次结构”寻找的。
    def cc(self):
        print("cc")

c = C()#因为C是多继承 实例c调用两个父类的方法优先调用B 符合类的层次结构
c.say()
print(C.mro())