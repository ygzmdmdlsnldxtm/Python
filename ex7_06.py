
'''Python的多态问题'''
#多态是方法的多态，属性没有多态
#必须继承和重写
#没有完全意义上的多态
class Man():
    def eat(self):
        print("饿啦，吃饭了.....")
class China(Man):
    def eat(self):
        print("中国人用筷子吃饭......")
class English(Man):
    def eat(self):
        print("英国人用刀叉吃饭.......")
class Indian(Man):
    def eat(self):
        print("印度人用右手吃饭........")
class Animal():
    def eat(self):
        print("动物吃饭不用手吃饭.......")
class Cat(Animal):
    def eat(self):
        print("我是小猫，我喜欢吃鱼......")
def manEat(m):
    if isinstance(m,Man):
        m.eat()
    else:
        print("不用手吃饭......")
    return
manEat(China())
manEat(English())
manEat(Cat())