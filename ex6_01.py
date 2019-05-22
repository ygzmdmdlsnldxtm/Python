#测试LEGB
str = "global str"
def outer():
    str = "outer"
    def inner():
        #str = "inner"
        print(str)#首先是在局部空间找str
    inner()

outer()