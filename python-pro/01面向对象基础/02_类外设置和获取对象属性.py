
class Car:

    def run(self):
        print("running")


c1 = Car()
# 设置属性
c1.name = "奔驰"
c1.price = 300000
c1.run()
print(f"{c1.name},{c1.price}")
