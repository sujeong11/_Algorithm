# 언어 : Python, (성공/실패) : 1/1, 메모리 : 156812KB, 시간 : 2208ms

import sys

N = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

x_sort = list(sorted(set(x)))

# 정렬 후 작은 값부터 인덱스를 부여
dic = {x_sort[i]: i for i in range(len(x_sort))}

for i in x:
    print(dic[i], end=' ')