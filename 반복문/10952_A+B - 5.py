# 언어: Python, (성공/실패) : 1/0, 메모리 : 30840KB, 시간 : 68ms

import sys

while (True):
    A, B = map(int, sys.stdin.readline().split())

    if(A == 0 and B == 0):
        break

    print(A + B)