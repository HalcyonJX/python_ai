# 字面量
{1, 3, 5, "haha", True, 3, 5}

# 变量
set1 = {1, 3, 5, "haha", True, 3, 5}
print(set1)  # 去重且无序

# 空集合
set1 = set()
print(set1)


"""
集合修改方法
"""
# 添加元素
my_set = {"a", "b", "c", "d"}
my_set.add("e")
print(my_set)

# remove(元素) 移除指定元素
my_set.remove("a")
print(my_set)

# pop() 随机取出一个元素返回
print(my_set.pop())
print(my_set)

# 清空集合
my_set.clear()
print(my_set)


# 两个集合的差集
set1 = {1, 2, 3}
set2 = {1, 4, 5}
set3 = set1.difference(set2)
print(set3)

# 在set1内，删除和set2相同的元素 set1被修改，set2不变
set1.difference_update(set2)
print(set1)
print(set2)

# 2个集合的并集，合并
set1 = {1, 2, 3}
set2 = {1, 4, 5}
set3 = set1.union(set2)
print(set3)

# 集合元素
print(len(set1))

# 遍历集合
for i in set1:
    print(i)
