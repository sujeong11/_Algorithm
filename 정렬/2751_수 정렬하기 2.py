# 언어 : Python, (성공/실패) : 1/1, 메모리 : 75672KB, 시간 : 1450ms

import sys

N = int(input())
nums = []

for i in range(N):
    nums.append(int(sys.stdin.readline()))

nums.sort()

for i in nums:
    print(i)