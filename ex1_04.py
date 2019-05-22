"""
while 循环问题
"""
n = 0
sum = 0
while True:
    sum+=pow(5,n)
    if sum>8000:
        print(n)
        break
    n=n+1
sum = 0
for i in range(1,11):
    for j in range(1,i+1):
        sum =sum + j
print(sum)