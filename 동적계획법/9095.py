import sys
input = sys.stdin.readline

dp = [0] * 11
dp[1] = 1 # 1
dp[2] = 2 # 1+1, 2
dp[3] = 4 # 1+1+1, 1+2, 2+1, 3
for i in range(4, 11): # 4부터는 (현재 값 -1)까지의 합이 값이 되는 규칙
    dp[i] = sum(dp[i-3:i])

T = int(input())
for _ in range(T):
    print(dp[int(input())])