# 언어: Python, (성공/실패) : 1/0, 메모리 : 30840KB, 시간 : 68ms

import sys

T = int(sys.stdin.readline());

for i in range (T):
    A, B = map(int, sys.stdin.readline().split());
    print("Case #{}: {} + {} = {}".format(i+1, A, B, A+B));