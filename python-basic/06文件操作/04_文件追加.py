
"""
a模式 append追加
文件不存在则创建
文件存在则在文件末尾追加
"""
f = open('./test.txt', 'a', encoding='utf-8')
f.write('\nHello World')
f.close()
