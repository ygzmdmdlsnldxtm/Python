
"""
for循环问题
"""
n = int(input("请输入宽度："))
for i in range(1,n+1):
    for j in range(i,n+i):
        print(j,end=" ")
    print()
n = int(input("请输入查询范围："))
count = 0
for i in range(1,n+1):
    if i%5!=0 and i%7!=0 and i%11!=0:
        count+=i
print(count)
打印圣诞树
n = int(input("请输入树干高度："))
for i in range(1,n+1):
    for j in range(0,2*i-1):
        print("*",end="")
    print()
for x in range(0,n):
    print("*",end='\n')