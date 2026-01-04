# 字符串的下标操作，正反向都支持
s = "helloworld"
print(s[5])
print(s[-5])

# 查找某元素在容器内的下标，找到返回下标，找不到报错
print(s.index("e"))

# replace(old_str, new_str)
s = "周杰伦|王力宏|刘德华"
s2 = s.replace("|", ",")
print(s2)

# split 按指定分隔符，将字符串分隔多份，存入list内
lst = s.split("|")
print(lst)

# strip() 去除字符串的前后空格和回车符
s = "    \nhelloWorld\n     "
print(s.strip())
s = "|||helloworld|||"
print(s.strip("|"))

# 统计字符串有多少个a
s = "dadasaaadaidajnasdminn"
print(s.count("a"))

# 统计字符串有多长
print(len(s))
