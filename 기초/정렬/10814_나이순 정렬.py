# 언어 : Python, (성공/실패) : 1/1, 메모리 : 45468KB, 시간 : 292ms

import sys

N = int(input())
info = []

for i in range(N):
    age, name = list(map(str, sys.stdin.readline().split()))
    age = int(age)
    info.append((age, name))

info.sort(key= lambda x:x[0])

for i in info:
    print(i[0], i[1])