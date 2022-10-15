# 언어 : Python, (성공/실패) : 1/5, 메모리 : 30840KB, 시간 : 10296ms

import sys

N = int(input())
# 계수 정렬을 이용해보자.
check = [0] * 10001

for i in range(N):
    num = int(sys.stdin.readline())
    check[num] = check[num] + 1

for i in range(10001):
    if check[i] != 0:
        for j in range(check[i]):
            print(i)