"""
如果文件不存在，则创建文件，如果存在，则清空文件内容
"""

# 打开
f = open('./test.txt', 'w', encoding='utf-8')
# 写入Hello World
f.write('Hello World')
# 将缓冲区的内容，写入到硬盘文件中
f.flush()
# 关闭
f.close()
