'''函数返回另一种函数，作为返回值'''
def get_fuction():
    s = input("请输入您需要的操作:   ")
    if s == "求最大":
        return max
    elif s == "求和":
        return sum
    elif s == "求最小":
        return min
L = [9,8,7,6]
f = get_fuction()
print(f(L))