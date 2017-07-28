import operator as op

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

# x = float(0.9037)
# total = 0
# while total < 0.5:
#     y = float(1.0) - float(x)
#     total = 0
#     print x, y 
#     for k in range(83):
#         sum = 0
#         if k == 0:
#             sum += ncr(82, 0)
#         else:
#             for n in range(1, k + 1):
#                 sum += (-1)**(n + 1) * ncr(k - 1, n - 1) * ncr(82 - n + 1, k - n + 1)
# #             print sum
#         total += x ** (82 - k) * y ** (k) * sum
# #         print 'tot:' + str(total)
#     x += 0.00001
#     print total

#p1a
# total = 0
# for k in range(83):
#     sum = 0
#     if k == 0:
#         sum += ncr(82, 0)
#     else:
#         for n in range(1, k + 1):
#             sum += (-1)**(n + 1) * ncr(k - 1, n - 1) * ncr(82 - n + 1, k - n + 1)
#         print sum
#     total += 0.8 ** (82 - k) * 0.2 ** (k) * sum
#     print 'tot:' + str(total)
# print total

#p1c
num_games = 82
total = 0
while total < 0.5:
    num_games -= 1
    total = 0
    for k in range(num_games + 1):
        sum = 0
        if k == 0:
            sum += ncr(num_games, 0)
        else:
            for n in range(1, k + 1):
                sum += (-1)**(n + 1) * ncr(k - 1, n - 1) * ncr(num_games - n + 1, k - n + 1)
        total += 0.8 ** (num_games - k) * 0.2 ** (k) * sum
    print total
    print num_games
print num_games
 


