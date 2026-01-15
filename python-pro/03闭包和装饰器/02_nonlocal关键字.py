"""
nonlocal 关键字用于在函数或其他作用域中使用外层(非全局)变量。
作用：
1. 修改外层变量
2. 在嵌套函数中返回一个函数，该函数使用外层变量
"""


def outer_func():
    a = 100

    def inner_func():
        nonlocal a
        a = a + 1
        print(a)

    return inner_func


f = outer_func()
f()
f()
f()
f()
