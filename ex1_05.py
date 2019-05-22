"""
打印倒三角形
"""
i = int(input("请输入一个数值："))
while True:
    print("*"*i)
    i -= 1
    if i == 0:
        break
"""
占位符 % 和类型码之间的格式语法:
"""
a = str(input("请输入第一行："))
b = str(input("请输入第二行："))
c = str(input("请输入第三行："))
print("%-20s"%a)
print("%-20s"%b)
print("%-20s"%c)