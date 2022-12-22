import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
dp = [0] * N
dp[0] = 1

# 도달할 수 있으면 1 아니면 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if dp[i] and (j - i) * (1 + abs(A[j] - A[i])) <= K:
            dp[j] = 1

print("YES" if dp[N - 1] else "NO")