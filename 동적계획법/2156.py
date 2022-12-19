import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input()) for _ in range(n)]
dp = [0] * n
dp[0] = wine[0]

# 인덱스 에러를 위한 예외처리
if n > 1:
    dp[1] = wine[0] + wine[1]
if n > 2:
    dp[2] = max(wine[0] + wine[2], wine[1] + wine[2], dp[1])
for i in range(3, n):
    # 1. 현재 잔 X 2. 현재, 전전 잔 O / 이전 잔 X 3. 현재, 이전 잔 O / 전전 잔 X
    dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])

print(dp[n-1])