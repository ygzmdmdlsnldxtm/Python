a = 10
def outer():
    b = 100
    def inner():
        nonlocal b
        b = 300
        print(b)

        #print("inner:b",b)

    inner()
    print("outer:b",b)
outer()
'''内置函数用于数据隐藏'''
def PrintName(isChinese,name,famliyname):
    def inner(a,b):
        print("{0} {1}".format(a,b))
    if isChinese:
        inner(famliyname,name)
    else:
        inner(name,famliyname)

PrintName(True,"镇东","吴")
PrintName(False,"Kobe","Bryant")