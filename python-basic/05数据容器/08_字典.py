# 字面量
print({
    "周杰伦": 99,
    "林俊杰": 77
})

# 空字典
d = {}
print(type(d))
d = dict()
print(type(d))

d = {"周杰伦": 99, "林俊杰": 77, "林俊杰": 66}
# 没有下标访问d[0]，本质是去找0这个key
# print(d[0])
print(d["周杰伦"])
# 字典key是不可以重复的，后面的key覆盖前面的
print(d)

# 新增元素
d["张学友"] = 24
print(d)
# 更新元素
d["张学友"] = 23
print(d)
# 移除元素
d.pop("林俊杰")
print(d)
# 获取所有key
x = d.keys()
print(type(x))
print(x)
# 遍历
for key in d.keys():
    print(key)
# 数量
print(len(d))
# 清空
d.clear()
print(d)
