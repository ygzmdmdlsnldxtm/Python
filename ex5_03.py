'''函数可以作为参数'''
def f1(fn):
    print("fn绑定的函数是：{}".format(fn))
def fn():
    return "hello,world"

f1(fn())
print("------------------")
def goodbye(L):
    for x in L:
        print("再见:", x)
    return "hello world"

def hello(L):
    for x in L:
        print("欢迎:", x)
    return "hello world"

def fx(fn):
    print("fx被调用{}".format(fn))

L = ['Tom','Jerry','Spike']
fx(hello(L))
fx(goodbye(L))