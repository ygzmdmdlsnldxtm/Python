"""
斐波那契数列
"""
def f(n):
    if n == 1 or n == 0:
        return 1
    else:
        return f(n-2)+f(n-1)
for i in range(0,6):
    print(f(i))

s = 'abc'
print(len(str(hash(s)))*4, hash(s))#第一个参数固定长度
print(len(s))
#打印三角形
n = int(input("请输入三角形宽度："))
for i in range(0,n):
    for j in range(2*i+1):
        print("*",end="")
    print()