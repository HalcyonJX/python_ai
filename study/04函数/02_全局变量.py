# 函数里使用全局变量，和修改
num = 100


def fuc_a():
    print(num)   #  全局


def fuc_b():
    num = 300
    print(num)


def fuc_c():
    global num
    num = 200
    print(num)


fuc_a()
fuc_b()
fuc_c()
