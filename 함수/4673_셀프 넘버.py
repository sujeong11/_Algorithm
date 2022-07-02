# 언어: Python, (성공/실패) : 1/2, 메모리 : 30840KB, 시간 : 552ms

def d(n):
    result = n

    while n != 0:
        result = result + n % 10
        n = n // 10

    return result

not_self_num = []

for i in range(1, 10001):
    not_self_num.append(d(i))
    if i not in not_self_num:
        print(i)