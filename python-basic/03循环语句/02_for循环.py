name = "Hello世界123"

for x in name:
    print(x, end=" ")

# range语句 可迭代对象
for i in range(10):
    print(i, end=" ")

print()
for i in range(101, 111):
    print(i, end=" ")

print()

for i in range(100, 1000, 100):  # 每次加100，不包括1000
    print(i, end=" ")
