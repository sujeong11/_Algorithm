# 언어: Python, (성공/실패) : 1/1, 메모리 : 30840KB, 시간 : 68ms

a, b = map(int, input().split())

if (a >= 1 and b <= 10000):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)