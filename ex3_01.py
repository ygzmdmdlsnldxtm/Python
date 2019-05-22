s = "hello"
j = ("-").join(s)
print(j)
L = []
L = [x for x in range(10) if x>5]
print(L)
s = "   sdf safe f"
z = s.split()
s = "".join(s.split())#join()：连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
print(z)
dict = {}
dict['birthday'] = (2001,1,1)
dict['name'] = "XiaoM"
dict['age'] = 16
del dict['age']
print(dict)