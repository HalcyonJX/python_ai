"""
类方法：
1. 类方法的第一个参数是cls，代表这个类本身
2. 类方法可以直接访问类的属性，调用类方法的时候，不需要实例化
3. 类方法中，既可以调用类属性，也可以调用实例属性
4. 类方法中，既可以调用类方法，也可以调用实例方法

静态方法：
1. 静态方法不需要访问类属性，也不需要访问实例属性
2. 静态方法中，既不能调用类属性，也不能调用实例属性
3. 静态方法中，既不能调用类方法，也不能调用实例方法
4. 静态方法中，既不能调用类方法，也不能调用实例方法
"""


class Person:
    country = 'china'

    @classmethod
    def eat(cls):
        print(cls.country)
        print(f'{cls}')
        print('eat')

    @staticmethod
    def run():
        print(Person.country)
        print('run')


if __name__ == '__main__':
    p1 = Person()
    p1.eat()
    p1.run()
    Person.eat()
    Person.run()
