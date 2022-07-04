# 언어 : Python, (성공/실패) : 1/0, 메모리 : 30840KB, 시간 : 72ms

import sys

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

for i in range (N):
    if (A[i] < X):
        print(A[i], end=' ')