"""
打印1~20的整数，每行5个数，打印四行
"""
count = 0
for i in range(1,21):
    print(i,end=' ')
    count+=1
    if count%5 == 0:
        print('\n')

a = 216
b = 16
c = a//b
d = a%b
print("216两是{}斤{}两".format(c,d))

print("请输入n的数值：")
n = int(input())
print("#"*n)
print("# #")
print("# #")
print("#"*n)
#如果长度是偶数就输出| 如果是基数就输出中间值
a = "sfaf5g"
if len(a)%2 == 0:
    print("|")
else:
    print(a[len(a)//2])
