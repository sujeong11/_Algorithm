# 언어: Python, (성공/실패) : 1/1, 메모리 : 30840KB, 시간 : 68ms

T = int(input())

for i in range(T):
    case = list(map(str, input().split()))
    result = ''

    for j in case[1]:
        result += j * int(case[0])

    print(result)
