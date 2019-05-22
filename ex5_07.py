
'''全局字典和局部字典'''
a = 500
b = 6000
def f():
    c = 300
    print('全局变量的字典：',globals())
    print('局部变量的字典：',locals())
f()
'''列表浅拷贝与深拷贝'''
import  copy
def testCopy():
    a = [20, 50, [5, 6]]
    b = copy.copy(a)
    print("a:",a)
    print("b:",b)
    b.append(30)
    b[2].append(9)
    print("浅拷贝.....")
    print('a:',a)
    print('b:',b)


def testdeepCopy():
    a = [20, 50, [5, 6]]
    b = copy.deepcopy(a)
    print("a:", a)
    print("b:", b)
    b.append(30)
    b[2].append(9)
    print("深拷贝.....")
    print('a:', a)
    print('b:', b)
testCopy()
testdeepCopy()
#可以理解为浅拷贝就是拷贝原体的第一层联系
#传递不可变对象时，发生赋值使用时浅拷贝 如下
a = (10,50,[8,96])
print('a:',id(a))
def test(m):
    print('m:',id(m))
    m[2][1] = 985
    print(m)
    print('m:',id(m))
test(a)
print(a)
'''求素数的新方法'''
def fn(n):
    L = []
    for i in range(2,n+1):
        flag = True
        for j in range(2,i):
            if i%j==0:
                flag = False
        if flag:
            L.append(i)
    return L
a = fn(11)
print(a)