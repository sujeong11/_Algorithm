# 사람 수와 관계없이 3종류 치킨으로만 시킴
from itertools import combinations

N, M = map(int, input().split())
prefer = [list(map(int, input().split())) for _ in range(N)]
max_sum = 0

for x, y, z in combinations(range(M), 3):
    sum = 0

    for i in range(N):
        sum += max(prefer[i][x], prefer[i][y], prefer[i][z])
    max_sum = max(max_sum, sum)

print(max_sum)