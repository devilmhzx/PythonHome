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
