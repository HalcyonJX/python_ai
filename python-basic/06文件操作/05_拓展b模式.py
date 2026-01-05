"""
b模式
二进制文件
"""
f = open('./test.txt', 'rb')
# f = open('./test.txt', 'wb')
content = f.read()
print(content)

f.close()
