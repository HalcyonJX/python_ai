def func(name, **kwargs):
    print(kwargs)


func("aa", id=1, age=11, addr="xx")


def func2(name, age, *args, **kwargs):
    print(f"元组收集：{args}")
    print(f"字典收集：{kwargs}")


func2("aa", 12, "xxx", "aaa", "ccc", gender="男", addr="重庆")
