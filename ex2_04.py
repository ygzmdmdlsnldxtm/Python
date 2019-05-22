"""
输入一个整数n 代表结束的数.
将 1 ~ n之间所有的素数计算出来并存入到列表L 中
1) 最后打印此列表中的全部素数
2) 打印这些素数的和
"""
list = []
n = int(input("请输入结束的数："))
for i in range(1,n+1):
    if i<2:
        continue
    for j in range(2,i):#如果range()方法里面的范围不正确就会不执行该for语句
        if i%j==0:
            break
    else:
        list.append(i)
print(list)
# sum = 0
# for x in list:
# #     sum+=x
# # print(sum)
"""
列表生成式  可迭代对象就是可以用for循环遍历的对象
"""
list = []
list = [x for x in range(1,100) if x * (x + 1) % 11 == 8]
print(list)
import math
print(math.sqrt(30))