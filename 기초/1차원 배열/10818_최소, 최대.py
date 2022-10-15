# 언어 : Python, (성공/실패) : 1/0, 메모리 : 148396KB, 시간 : 408ms

import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

print(min(nums), max(nums))