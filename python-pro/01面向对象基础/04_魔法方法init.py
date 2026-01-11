"""
Python 魔法方法，在满足特定条件时，自动调用
__init__ 初始化方法
"""


class Car:
    def __init__(self, name, price):
        """
        :param name: 车名
        :param price: 价格
        """
        self.name = name
        self.price = price

    def run(self):
        print("running")

    def show(self):
        print(f"{self.name},{self.price}")


c1 = Car("奔驰", 300000)
c1.run()
c1.show()
