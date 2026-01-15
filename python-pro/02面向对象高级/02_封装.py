"""
在Python中，可以为属性和方法设置私有权限，只允许在类内部被调用。
在属性名或方法名前加__，表示该属性或方法为私有属性或方法。
"""


class Person:
    # 私有属性
    __name = "jack"
    __age = 20

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # 私有方法
    def __show(self):
        print(f"{self.__name},{self.__age}")

    def show(self):
        self.__show()


p = Person("Tom", 10)
p.show()
