import sys
input = sys.stdin.readline

dp = [0] * 1001
dp[1] = 1
dp[2] = 2
# 3부터는 (현재 값 - 1) + (현재 값 - 2)이 값이 되는 규칙
for i in range(3, 1001):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[int(input())] % 10007)