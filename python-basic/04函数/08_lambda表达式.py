
def func(compute):
    result = compute(3, 4)
    print(result)


func(lambda x, y: x * y)
func(lambda x, y: x + y)

# 如果想要重复利用
jianfa = lambda x, y: x - y
func(jianfa)

