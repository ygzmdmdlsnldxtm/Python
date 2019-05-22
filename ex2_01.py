"""
Python 类 方法 实例化
"""
#非递归解法
class Test():
    def Function(self, begin, end):
        count = 0
        self.begin = begin
        self.end = end
        for i in range(begin,end+1):
            print(i,end=" ")
            count+=1
            if count % 5 == 0:
                print('\n')
function = Test()
function.Function(8,30)