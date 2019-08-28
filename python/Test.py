# b = set()
# while True:
#     a = int(input('请输入多个整数：'))
#     if a < 0:
#         break
#     b.add(a)
# print('输入的不同整数数量为：%d' % len(b))
# print('剩下的输入的整数和为：%d' % sum(list(b)))

# def print_even(n):
#     # for i in range(0, n):
#     #     if i % 2 == 0:
#     #         print(i, end=' ')
#     for i in range(0, n, 2):
#         print(i, end=' ')
#
#
# a = int(input('请输入一个整数：'))
#
# print_even(a)

# list1 = [0, 1, 2, 3]
# list2 = ['libi', 'bilii', 'liwei', 'aini']
# #双巡回推导式
# dict_list = {x: y for x in list1 for y in list2}
# print(dict_list)
# #{0: 'aini', 1: 'aini', 2: 'aini', 3: 'aini'}

# def myadd(a, b, c=0, d=0):
#     print(a + b + c + d)
#
# myadd(2, 8)

# def mysum(*args):
#     return sum(args)
#
#
# print(mysum(1, 2, 3, 4, 5))
# ----------------------------------------------------------


# def isprime(x):
#     if str.isdigit(x):
#         if int(x) % 2 == 0:
#             return False
#         else:
#             return True
#     else:
#         print('输入的%s不是数字' % x)
#
#
# def prime_m2n(m, n):
#     if str.isdigit(m) and str.isdigit(n):
#         r = list()
#         for i in range(int(m), int(n)):
#             if i % 2 == 1:
#                 r.append(i)
#         return str(r)
#     else:
#         print('输入的%s不是数字' % n)
#
#
# def primes(n):
#     if str.isdigit(n):
#         return list(range(1, int(n), 2))
#     else:
#         print('输入的%s不是数字' % n)
#
#
# def myrange(a, *args):
#     if not args:
#         print(list(range(a)))
#     elif len(args) == 1:
#         print(list(range(a, args)))
#     elif len(args) == 2:
#         print((list(range(a, args[0], args[1]))))
#     else:
#         print('输入错误!')
#
#
# m = input('请输入一个整数m：')
# if isprime(m):
#     print('这是一个素数！')
# else:
#     print('这不是一个素数')
# print('0到%s' % m + '之间的素数为：' + str(primes(m)))
# n = input('请再输入一个整数n，比之前的大：')
# print('m到n之间的素数为：' + str(prime_m2n(m, n)))
# myrange(3)
# myrange(3,9)


# a = 12
# b = [1, 2]
#
#
# def ces(x, y):
#     # 想要修改全局作用域变量需要在千米加 global 来声明为此变量是全局变量
#     global a, b
#     a += x
#     b.append(y)
#
#
# ces(10, 5)
# print(a)
# print(b)

# fx = lambda n: ((n ** 2) + 1) % 5 == 0
#
# print(fx(3))
# print(fx(4))
#
# mymax = lambda x, y: max(x, y)
#
# print(mymax(100, 200))

# def mysum(x):
#     a = 1
#     for i in range(a, x + 1):
#         a += i
#     return a
#
#
# def myfuc(n):
#     a = 1
#     for i in range(a, n + 1):
#         a *= i
#     return a
#
#
# def myfun(n):
#     a = 1
#     if n == 1:
#         return a
#     if n > 1:
#         for i in range(2, n+1):
#             a = i ** 2 + a
#         return a
#
#
# print(mysum(10))
# print(myfuc(4))
# print(myfun(4))


# a = 0
#
#
# def powsum(x):
#     global a
#     for i in range(0, x + 1):
#         a += pow(i, 2)
#     return a
#
#
# powsum(9)
# print(a)
#
# b = 0
#
#
# def powsum2(x):
#     global b
#     for i in range(0, x + 1):
#         b += pow(i, 3)
#     return b
#
#
# powsum(9)
# powsum2(9)
# print(b)
#
# c = 0
#
#
# def powsum3(x):
#     global c
#     for i in map(pow, range(1, x + 1), range(x, 0, -1)):
#         c += i
#     return c
#
#
# powsum3(9)
# print(c)

# 第归求和
# def mysum(n):
#     if n == 1:
#         return 1
#     return n + mysum(n-1)
#
# print(mysum(100))

# 阶乘计算和
# def jiechen(n):
#     if n == 1:
#         return 1
#     return n * jiechen(n - 1)
#
#
# m = 0
# for i in range(1, 4):
#     m += jiechen(i)
# print(m)

# L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]

# print(len(L))

# for i in L:
#     if type(i) is list:
#         for x in i:
#             if type(x) is list:
#                 for n in x:
#                     print(n)
#             else:
#                 print(x)
#     else:
#         print(i)

# def mydeco(fn):
#     def fx():
#         print('+++++++++++++++')
#         fn()
#         print('---------------')
#
#     return fx
#
#
# # 装饰器
# @mydeco
# def myfunc():
#     print('这是一个测试！')
#
#
# myfunc()

# ---------------------------------------------
# from time import *
#
#
# def myfn(n):
#     '''
#     #每隔一秒在屏幕中打印一次，共打印n次
#     :param n: 打印次数
#     :return: 返回打印的内容
#     '''
#     if n > 0:
#         print('Hello world')
#         sleep(1)
#         myfn(n - 1)

# myfn(3)

# a = myfn

# print(a.__name__)
# print(myfn.__name__)
# ------------------------------------
# import random
#
# x = random.randrange(0, 100)
# ran_a = 0
# while True:
#     y = int(input('请输入一个数字猜猜：'))
#     if y > x:
#         print('大了～')
#         ran_a += 1
#     elif y < x:
#         print('小了')
#         ran_a += 1
#     else:
#         print('猜对了！')
#         ran_a += 1
#         break
#
# print('猜对的次数为：%d' % ran_a)

# 使用try判断错误
# def get_score():
#     x = 0
#     s = input('请输入成绩：')
#     try:
#         x = int(s)
#     except ValueError as xxx:
#         print('输入的成绩有错误！错误代码为：', xxx)
#     if x in range(100):
#         return x
#     else:
#         return 0
#
#
# score = get_score()
# print("学生的成就是：", score)

# ----------------文件读取--------------------------------
# try:
#     myfile = open('myfile.txt')
#     while True:
#         osFile = myfile.readline()
#
#         # print(osFile.rstrip(''))
#         oslist = osFile.rstrip('\n').split(',')
#         # print(oslist)
#         if oslist == ['']:
#             break
#
#         print('{}今年{}岁，成绩是：{}'.format(oslist[0], oslist[1], oslist[2]))
#
#     myfile.close()
# except IOError:
#     print('文件打开失败')

# ----------------------------------------------------------------
