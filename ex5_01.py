'''
可改变字符串
'''
import  io
s = "hello world"
sio = io.StringIO(s)
sio.seek(7)
print(sio.getvalue())
sio.write("G")#如果没有使用seek()方法 默认更改的是第一位字符对象
print(sio.getvalue())