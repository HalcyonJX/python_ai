"""
函数式编程
"""


def func(compute):
    result = compute(1, 2)
    print(result)


def compute(x, y):
    return x * y


func(compute)
