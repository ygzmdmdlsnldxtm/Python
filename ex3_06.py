"""
星号元组形参:
"""
def func(*args):
    print("实参个数是:", len(args))
    print("args的值是:", args)
func(1, 2, 3)
func("ABCD", 3.14, 100, True, None)
def myfun2(b, *args, c, d):#*args是其他参数
    print("b=", b)
    print("args=", args)
    print("c=", c)
    print("d=", d)
myfun2(100, 200, 300, 400, d=600, c=500)
def func(**kwargs):
    print("关键字传参的个数是:", len(kwargs))
    print("kwargs=", kwargs)
func(name='home', age=15)
func(a=1, b="BBBB", c=[2, 3, 4], d=True)

def function(c,*a,k):
    print("a=",a)
    print("k=",k)
    print("c=",c)

function(100,50,40,k=100)
def f(x,*,h):
    print("x=",x)
    print("h=",h)
f(100,h=7)