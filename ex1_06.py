
"""
for 循环问题
"""
n = int(input("请输入正方形宽度："))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()
"""
Python 类 方法 实例化
"""
#递归解法
class Test():
    def Function(self, begin, end,count = 0):
        self.begin = begin
        self.end = end
        if begin > end:
            return
        if count%5==0:
            print('\n')
        print(begin,end=" ")

        self.Function(begin + 1, end,count+1)#如果不添加self就会提示Function未定义
function = Test()
function.Function(8,30)
