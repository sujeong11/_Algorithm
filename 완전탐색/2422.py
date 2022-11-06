from itertools import combinations

N, M = map(int, input().split())
ice = [[False] * N for _ in range(N)]
result = 0

for i in range(M): # 섞어 먹으면 안 되는 조합 True로 표시
    x, y = map(int, input().split())
    ice[x-1][y-1] = True
    ice[y-1][x-1] = True

# 섞어 먹으면 안되는 조합이 포함되어 있을 시 건너뛰며 카운트
for comb in combinations(range(N), 3):
    if ice[comb[0]][comb[1]] or ice[comb[0]][comb[2]] or ice[comb[1]][comb[2]]:
        continue
    result += 1

print(result)