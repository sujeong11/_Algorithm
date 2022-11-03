# 파이썬의 itertools의 permutations를 활용해서 풀 수 있는 문제
N, M = map(int, input().split())
cards = list(map(int, input().split()))
result = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            num = cards[i] + cards[j] + cards[k]

            if (num > M):
                continue
            else:
                result = max(result, num)

print(result)