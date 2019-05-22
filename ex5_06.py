
'''函数作为参数实例'''
def f1():
    print("hello")
def f2(f):
    print(f)
    print(f"这是f2函数{f1}")
def outer():
    def inner():
        print("内部嵌套的函数")
    return f1

outer()()
print(outer)