import sys
input = sys.stdin.readline

dp = [0] * 1001
dp[1] = 1
dp[2] = 3
# 규칙: 3부터는 (i - 1) + (i - 2) * 2
for i in range(3, 1001):
    dp[i] = dp[i - 1] + (dp[i - 2] * 2)

print(dp[int(input())] % 10007)