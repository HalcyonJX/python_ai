list1 = ["周杰伦", "林俊杰", "张杰", "Faker", "Zeus", "Oner", "Gumayusi", "Keria"]

# 根据元素查找列表索引位置
print(list1.index("Zeus"))
# 确认元素是否在列表内
print("666" in list1)
print("Faker" in list1)
# 修改指定下标的元素值
list1[2] = "JackeyLove"
print(list1)
# 插入元素
list1.insert(2, "Viper")  # 索引超过大小放在最后
print(list1)
# 在尾部新增
list1.append("Bang")
print(list1)
# 在尾部新增一批元素
lst = [1, 2, 3]
lst.extend([4, 5, 6])
print(lst)
# 删除元素 按下标
del lst[0]
print(lst)
lst.pop(0)
print(lst)
# 删除元素 按元素
my_list = [1, 1, 1, 2, 3, 4]
my_list.remove(2)
print(my_list)
# 清空列表内容
my_list.clear()
print(my_list)
# 统计某元素在列表内的数量
my_list = [1, 2, 2, 2, 1]
print(my_list.count(1))
print(my_list.count(2))
# 统计列表内元素的数量
print(len(my_list))
