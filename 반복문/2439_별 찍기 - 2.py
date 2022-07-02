# 언어: Python, (성공/실패) : 1/0, 메모리 : 30840KB, 시간 : 68ms

import sys

N = int(sys.stdin.readline());

for i in range(1, N+1):
    print("{}{}".format((N-i) * ' ', i * '*'));