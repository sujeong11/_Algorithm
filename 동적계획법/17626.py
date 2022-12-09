# PyPy3로 해야 시간 초과가 발생하지 않음
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    min_val = 4 # 제곱 수의 최대 개수가 4이므로

    for j in range(1, int(i ** 0.5) + 1):
        min_val = min(min_val, dp[i - j ** 2])
    dp[i] = min_val + 1

print(dp[n])