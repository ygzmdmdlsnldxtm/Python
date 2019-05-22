"""
字典推导式:
作用：
用可迭代对象生成字典
语法:
{键表达式 : 值表达式 for 变量 in 可迭代对象 [if 真值表达式]}
注: []的内容代表可省略
"""
L = ["tarena","xiaozhang","hello"]
dict = {x:len(x) for x in L}
print(dict)
no = [1001,1002,1003,1004]
names = ['Tom','Jerry','Spike','Tyke']
dict = {no[i] : names[i] for i in range(4)}
print(dict)
用集合方法去除多余元素
number = (1,2,3,4,5,5,7,8,9,9,1)
s = {x for x in number}
print(s)
a = list(input("请输入字符串："))

d = {}
for x in a:
    if not x in d:
        d[x] = 1
    else:
        d[x] = d[x] + 1

print(d)#利用 not in 判断元素出现的次数
class Test():
    def __init__(self):
        self.name = "吴镇东"
    def say(self):
        print("我的名字：{}".format(self.name))
    def count(self,no):
        if no == 1:
            return 1
        else:
            return self.count(no-1)*2+2
    def add(self,first,last,sum = 0):
        self.first=first
        self.last = last
        sum = first+last
        print(sum)

a = Test()
print(a.count(10))
a.add(1,54)
a.say()