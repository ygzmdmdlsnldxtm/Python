"""
求水仙花数
"""
#解法一
list = []
for x in range(100,1000):
    a = x // 100
    b = x % 100 // 10
    c = x % 10
    if x == a ** 3 + b ** 3 + c ** 3:
        list.append(x)
print(len(list))
#解法二
list1 = []
for x in range(100,1000):
    a = str(x)#将数字字符串化得到一个字符串方便取值
    if int(a[2])**3+int(a[1])**3+int(a[0])**3 == x:
        list1.append(x)
print(len(list1))
set()#删除列表中重复的元素