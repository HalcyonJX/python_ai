
f = open('./test.txt', 'r', encoding='utf-8')
for line in f:
    print(line.strip())
f.close()

# with 语句 自动关闭文件
with open('./test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())
