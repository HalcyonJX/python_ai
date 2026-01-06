def say_hi():
    print('hello world')


def wangwang():
    print("汪汪")


def add(x, y):
    return x + y


# wangwang()

"""
如果本文件被直接执行，则内置变量__name__的值为__main__
如果本文件被导入，则内置变量__name__的值为模块名
__name__是python一个内置变量，任何模块都有这个变量
我们可以通过这个变量来判断当前模块是否被直接执行
"""
if __name__ == '__main__':
    wangwang()
