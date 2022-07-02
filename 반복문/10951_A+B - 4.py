# 언어: Python, (성공/실패) : 1/1, 메모리 : 30840KB, 시간 : 68ms

import sys

while (True):
    try:
        A, B = map(int, sys.stdin.readline().split());
        print(A + B);
    except:
        break;