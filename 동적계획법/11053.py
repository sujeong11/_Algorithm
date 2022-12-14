import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N): # 현재 위치
    for j in range(i): # 이전의 위치들
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1) # 증가부분 수열 중 가장 긴 수열의 값에 1을 더한 것

print(max(dp))