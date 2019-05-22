'''重写str方法'''
class Person():
    def __init__(self,name):
        self.__name = name

    def __str__(self):
        return "名字是：{}".format(self._Person__name)
p = Person("吴川枫")
print(p)
#<__main__.Person object at 0x000002274402CD30>这是__str()__方法