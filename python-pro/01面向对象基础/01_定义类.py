# 定义一个类
class Person:
    # 属性

    # 行为
    def eat(self):
        print("吃饭")
        print(f"{self}")


# 实例化对象
p1 = Person()
p1.eat()
p2 = Person()
p2.eat()

"""
self 指向当前对象
"""