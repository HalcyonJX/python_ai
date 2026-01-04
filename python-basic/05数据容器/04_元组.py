# 字面量
(1, 3, 5, "haha")

# 变量
t1 = (1, 2, 3, "65")
print(t1, "类型：", type(t1))

# 空的元组
t2 = ()
t3 = tuple()
print(t2, type(t2))
print(t3, type(t3))

# 只有1个元素的元组（特殊写法）
t1 = (1, )  # 只有1个元素，也要写一个逗号
print(t1, type(t1))

"""
元组的相关操作
"""

# 根据下标取出数据
t1 = (1, 2, 'hello')
print(t1[2])

# 查找特定元素的第一个匹配项
t1 = ('hello', 'world', 1, 2, 3)
print(t1.index('world'))

# 统计某个数据在元组内出现的次数
t1 = (1, 2, 'hello', 3, 4, 'hello')
print(t1.count('hello'))

# 统计元组的个数
print(len(t1))

"""
不可以修改元组的内容，否则直接报错，但是可以修改元组内的list的内容（增删改等）
"""
t1 = (1, 2, ['hello', 'world'], 3, 4, 'hello')
t1[2][0] = "你好"
print(t1)
