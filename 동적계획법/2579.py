import sys
input = sys.stdin.readline

score = [0] * 301
dp = [0] * 301

N = int(input())
for i in range(N):
    score[i] = int(input())

dp[0] = score[0]
dp[1] = score[0] + score[1]
dp[2] = max(score[0] + score[2], score[1] + score[2])
# 마지막 계단을 반드시 밟아야 하므로 마지막 계단의 전 계단을 1. 밟은 경우 2. 밟지 않은 경우
for i in range(3, N):
    dp[i] = max(dp[i - 3] + score[i - 1] + score[i], dp[i - 2] + score[i])

print(dp[N - 1])