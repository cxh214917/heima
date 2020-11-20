i = 2
result = 0
while i <= 100:
    result += i
    i += 2
print('1-100之间的偶数和是:{}'.format(result))


j = 1
result1 = 0
while j <= 100:
    j += 1
    if j % 2 == 0:
        result1 += j
print('1-100之间的偶数和是:{}'.format(result1))
