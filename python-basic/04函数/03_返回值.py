# 多个返回值

def func():
    # 本质是返回了(1,2)的元组
    return 1, 2


x, y = func()   # 自动解包了
print(x, y)


