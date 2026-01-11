"""
子类重写父类方法
子类出现和父类同名属性、方法，会覆盖父类属性和方法
"""


class Father:
    def __init__(self):
        self.name = "father"
        self.age = 30

    def show(self):
        print("父类方法")
        print(f"{self.name},{self.age}")


class Son(Father):
    def __init__(self):
        super().__init__()
        self.name = "son"
        self.age = 10

    def show(self):
        super().show()
        print("子类方法")
        print(f"{self.name},{self.age}")


s = Son()
s.show()
