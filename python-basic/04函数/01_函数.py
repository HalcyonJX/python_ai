name = "HelloWorld"
length = len(name)
print(length)


# 手写一个获取字符串长度的函数
def my_len(data):
    len1 = 0
    for i in data:
        len1 += 1
    return len1


print(my_len(name))


def hello():
    print("你好 我是周杰伦")  # 其实会返回None


hello()

# None如果在if判断中，作为False
if not None:  # 非是not
    print("False")
