"""
基本语法：
try:
    可能发生异常的代码
except:
    如果出现异常，执行的代码
"""

f = None
try:
    f = open('./test.txt', 'r', encoding='utf-8')
except:
    print('文件不存在')

"""
捕获特定异常
"""
try:
    1 / 0
except ZeroDivisionError as e:
    print('除0错误')
    print(e)

"""
捕获多个异常
"""
try:
    1 / 0
except (ZeroDivisionError, NameError) as e:
    print(e)

# 捕获多个异常，同时区分
try:
    1 / 1
except ZeroDivisionError as e:
    print('除0错误')
    print(e)
except NameError as e:
    print('NameError错误')
    print(e)
else:
    print('没有异常')
finally:
    print('无论是否异常，都会执行')
