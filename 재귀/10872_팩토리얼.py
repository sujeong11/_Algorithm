# 언어: Python, (성공/실패) : 1/0, 메모리 : 30840KB, 시간 : 68ms

N = int(input())
result = 1

if (N > 0):
    for i in range(1, N+1):
        result = result * i

print(result)
