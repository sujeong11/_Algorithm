# 언어: Python, (성공/실패) : 1/0, 메모리 : 30840KB, 시간 : 92ms

T = int(input())

for i in range(T):
    case = input()
    sum = 0
    count = 1

    for i in case:
        if (i == 'O'):
            sum += count
            count += 1
        else:
            count = 1

    print(sum)

