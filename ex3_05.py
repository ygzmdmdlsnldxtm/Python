"""
打印完美数
"""
list = []
for i in range(1,10000):
    for n in range(1,i):
        if i%n==0:
            list.append(n)
    if sum(list) == i:#求和
        print(i)
    list=[]#清空用于下一次循环
#打印特殊三角形
n = int(input("请输入数字："))
for i in range(0,n):
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(i+1,0,-1):
        print(k,end=" ")
    print()
for a in range(n,0,-1):
    for b in range(1,a-1):
        print(b,end=" ")
    for c in range(a-1,0,-1):
        print(c,end=" ")
    print()
class Test():
    list = []
    def print_even(self,n):
        self.n=n
        self.list = [x for x in range(1,n) if x%2==0]
        return self.list
a = Test()
print(a.print_even(9))


L = []
while True:
    n = int(input("请输入："))
    if n < 0:
        break
    else:
        L.append(n)

print(max(L))
print(sum(L))
def fn(a,lst=[]):
    lst.append(a)
    print(lst)
l = [1,2,3,4]
fn(5,l)
fn(1.1)