def user_info(name, age, gender="女"):  # 可以提供默认值  默认值参数必须在无默认值参数的右边
    print(f"我是{name}，今年{age}岁，性别{gender}")


# 位置调用
user_info("小明", 20, "男")

# 关键字调用
user_info(age=20, gender="女", name="小帅")
