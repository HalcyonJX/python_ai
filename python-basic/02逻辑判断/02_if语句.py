age = int(input("请输入你的年龄："))
if 18 <= age < 30:
    print("你已经是一个成年人了")
elif age >= 30:
    print("三十而立")
else:
    print("你还小，多读书")


print("猜数字游戏")
num = 10
if int(input("请猜测第一个数字：")) == num :
    print("猜中了")
elif int(input("请猜测第二次：")) == num:
    print("猜中了")
elif int(input("请猜测第三次：")) == num:
    print("猜中了")
else:
    print("没猜中")