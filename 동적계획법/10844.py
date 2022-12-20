import sys
input = sys.stdin.readline

N = int(input())
dp = [[0] * 10 for _ in range(N+1)]

# 자릿수가 1일 때, 주의) 0으로 시작할 수 없으므로 dp[1][0]은 0으로 초기화
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        if j == 0: # 뒷자리가 0일 때는 앞에 1만 올 수 있다.
            dp[i][j] = dp[i - 1][1]
        elif j == 9: # 뒷자리가 9일 때는 앞에 8만 올 수 있다.
            dp[i][j] = dp[i - 1][8]
        else: # 뒷자리가 2 ~ 8일 때는 앞에 2개씩 올 수 있다. +1 또는 -1
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[N]) % 1000000000)