"""
列表练习
"""
list = []
sum = 0
sum1 = 0
while True:
    x = int(input("请输入X："))
    if x == -1:
        break
    else:
        list.append(x)
print(list)
for i in list:
    sum+=i
print(f"sum等于{sum}")
list2 = set(list)
print(list2)
for a in list2:
    sum1+=a
print("sum1等于{}".format(sum1))
list3 = []
for i in list:
    if list.count(i) == 2:
        list3.append(i)
print(set(list3))

dict = {}
dict['birthday'] = (2001,1,1)
dict['name'] = "XiaoM"
dict['age'] = 16
for key,value in dict.items():
    print(value,key)