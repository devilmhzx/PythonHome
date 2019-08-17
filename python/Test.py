# b = set()
# while True:
#     a = int(input('请输入多个整数：'))
#     if a < 0:
#         break
#     b.add(a)
# print('输入的不同整数数量为：%d' % len(b))
# print('剩下的输入的整数和为：%d' % sum(list(b)))


def print_even(n):
    # for i in range(0, n):
    #     if i % 2 == 0:
    #         print(i, end=' ')
    for i in range(0, n, 2):
        print(i, end=' ')


a = int(input('请输入一个整数：'))

print_even(a)
