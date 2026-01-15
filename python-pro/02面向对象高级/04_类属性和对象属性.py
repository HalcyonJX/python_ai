"""
类属性：
    类属性在类中定义，在方法的外部
    类属性用来记录与这个类相关联的属性，保存与这个类相关的数据
    类属性可以通过类名.属性名访问
    类属性可以通过实例对象.属性名访问
    类属性可以通过实例对象.属性名修改 但是修改的是实例对象的属性，不会影响类属性
    类属性可以通过类名.属性名修改 但是修改的是类属性，不会影响实例对象的属性
"""


class Person:
    country = "中国"

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Tom", 10)
print(p.name)
print(p.age)
print(p.country)
print(Person.country)
p.country = "美国"
print(p.country)
print(Person.country)
Person.country = "美国"
print(Person.country)
