"""
__all__ 是用来控制模块导入的
如果你不写__all__，from 模块名 import *那么模块中所有的函数和变量都会被导入
如果你写了__all__，from 模块名 import *那么只有__all__中指定的函数和变量才会被导入
"""
__all__ = ["wangwang", "hi"]


def wangwang():
    print("汪汪")


def hi():
    print("hi")


def info():
    print("info")
