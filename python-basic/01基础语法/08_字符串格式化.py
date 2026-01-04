# 字符串格式化 - 占位符
name = '周杰伦'
age = 11
message = '我是%s，今年%s岁' % (name, age)
print(message)

# 不同类型对应的占位符 %s  字符串   %d 整数  %f  浮点数
message1 = '我是%s，今年%d岁' % (name, age)
print(message1)

# 精度控制
height = 175.5557
message2 = "我的身高是：%10.3f" % height  # 占了10位，3个小数点，限制宽度少于实际宽度，不生效
print(message2)

# f_format格式化方法
message3 = f"我是{name}，今年{age}岁，身高{height}厘米"
print(message3)
# f_format精度控制
message4 = f"我是{name}，今年{age}岁，身高{height:10.3f}厘米"
print(message4)
