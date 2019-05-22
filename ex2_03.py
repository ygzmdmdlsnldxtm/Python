"""
List列表
"""
a=[]
for i in range(20013,20050):
   n = chr(i)
   a.append(n)
print(a)
#判断素数
n = int(input("请输入一个数："))
if n == 2:
    print("{}是素数".format(n))
else:
    for i in range(2, n+1):
        if n % i == 0:
            print("{}不是素数".format(n))
            break
        else:
            print("{}是素数".format(n))
            break
#[表达式 for 变量 in 可迭代对象]或[表达式 for 变量 in 可迭代对象 if 真值表达式]
begin = int(input("请输入begin："))
end = int(input("请输入end："))
L = [x for x in range(begin,end)if (x**2+1)%5==0]
print(L)