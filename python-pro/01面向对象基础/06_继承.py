"""
写法：
class 子类(父类):
    pass
python里可以单继承，也可以多继承，所有类最终都会继承object类
"""


class Father:
    def __init__(self):
        self.gender = "男"

    def walk(self):
        print("walking")


class Child(Father):
    pass


c = Child()
print(c.gender)
c.walk()


# 多继承
class Mother:
    def __init__(self):
        self.gender = "女"

    def sing(self):
        print("singing")


class Son(Father, Mother):
    pass


s = Son()
print(s.gender)  # 谁离子类最近，谁的属性就被继承了
s.walk()
s.sing()
