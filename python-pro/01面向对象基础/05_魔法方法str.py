"""
__str__方法：
    当使用print输出对象的时候，默认会调用对象的__str__方法来输出内容，如果不重写__str__方法，则会输出对象的地址。
__del__方法：
    当删除对象时，会自动调用__del__方法
    没有手动删除时，运行到文件结束才会被删除
"""


class Car:

    def run(self):
        print("running")

    def __str__(self):
        return "奔驰"

    def __del__(self):
        print("del")


c1 = Car()
print(c1)
print("程序结束了")
