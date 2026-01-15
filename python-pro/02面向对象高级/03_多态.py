"""
多态：同一个函数，接收不同的参数，实现不同的功能
实现多态的三个条件：
1. 继承
2. 重写
3. 父类引用指向子类对象
"""


# 1. 定义动物类
class Animal:
    def eat(self):
        pass


# 2. 定义猫类
class Cat(Animal):
    def eat(self):
        print("猫吃鱼")


class Dog(Animal):
    def eat(self):
        print("狗吃肉")


def make_eat(animal: Animal):
    animal.eat()


if __name__ == '__main__':
    make_eat(Dog())
    make_eat(Cat())
