
'''def在函数内部动态创建一个函数'''
def get_func(value):
    if value == 1:
        def myadd(x,y):
            return x+y
        return myadd
    if value == 2:
        def mysub(x,y):
            return x-y
        return mysub

fx = get_func(1)
print(fx(400,300))
fy = get_func(2)
print(fy(400,300))