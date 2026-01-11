
class Car:

    def run(self):
        print("running")

    def show(self):
        print(f"{self.name},{self.price}")


c1 = Car()
c1.name = "奔驰"
c1.price = 300000
c1.run()
c1.show()

c2 = Car()
c2.run()
# c2.show()  # 报错
