"""
1. 打开文件
2. 读取文件
3. 关闭文件
"""
# r模式，只读模式，不能写入
# 相对路径
f = open('./test.txt', 'r', encoding='utf-8')  # 打开

# print(f.read(3))  # 读取3个长度  下次读取从上次读取的下一个字符开始
# print(f.read(3))
# print(f.read())  # 读取所有 指针没有移动
# # 重置指针
# f.seek(0)
# print(f.read())


# readlines() 读取所有行
# for line in f.readlines():  # 默认不会去掉\n，需要调用strip()
#     line = line.strip()
#     print(line)


# readline() 读取一行
print(f.readline().strip())
print(f.readline().strip())


f.close()  # 关闭
