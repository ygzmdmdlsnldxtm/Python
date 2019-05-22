'''
三元表达式
'''
#拆分的形式，便于理解
def max (a,b,c):
    t = a if a > b else b
    return t if t > c else c
#L = dict(input("请输入："))
L = {'a':8,'b':9,'c':15}
print(max(**L))
print("**************************")
L1 = {'x':6,'y':84,'z':99}
def max1(x,y,z):
    return (x if x > y else y) if  (x if x > y else y) > z else z

print(max1(**L1))