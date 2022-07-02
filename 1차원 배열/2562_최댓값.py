# 언어: Python, (성공/실패) : 1/0, 메모리 : 30840KB, 시간 : 68ms

import sys

arr = []

for i in range(9):
    x = int(sys.stdin.readline())
    arr.append(x)

max_num = max(arr)

print(max_num)
print(arr.index(max_num)+1)