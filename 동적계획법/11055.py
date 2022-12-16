import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = A[:]

for i in range(1, N): # 현재 위치
    for j in range(i): # 이전의 위치들
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp))