import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)

# 1일 때는 이미 1이므로 연산이 필요하지 않아 시작점을 2로 두었다.
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1 # 이전 연산 결과에 -1을 연산한 것을 더 해준 것

    # 나눠보며 더 작은 값이 있나 확인하는 부분
    # if-else를 사용하지 않아야 3가지 연산을 다 거칠 수 있다.
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[N])