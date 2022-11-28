from itertools import combinations

N = int(input())
taste = [list(map(int, input().split())) for _ in range(N)]
combi = [combinations(taste, i) for i in range(1, N+1)] # 모든 조합 구하기
result = 1e9

for c in combi:
    for t in c:
        sour, bitter = 1, 0

        for s, b in t:
            sour *= s
            bitter += b

        result = min(result, abs(sour - bitter))

print(result)