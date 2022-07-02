# 언어: Python, (성공/실패) : 1/1, 메모리 : 30840KB, 시간 : 68ms

import sys

N = int(sys.stdin.readline())
num = N
count = 0

while (True):
    x = num // 10
    y = num % 10
    z = (x + y) % 10
    num = (y * 10) + z
    count += 1

    if (num == N):
        print(count)
        break