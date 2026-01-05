
def func(name, *xxx):
    print(f"我们是：{name}，我们的成员有：")
    for i in xxx:
        print(i)


func("T1", "Zeus", "Oner", "Faker", "Gumayusi", "Keria")
