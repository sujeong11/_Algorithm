import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)] # 해당 위치를 방문할 수 있는 횟수
dp[0][0] = 1

for i in range(N):
    for j in range(N):

        if (i == N - 1) and (j == N - 1): # 오른쪽 맨 끝점이라면
            print(dp[i][j])
            break

        # 오른쪽으로 이동
        if j + graph[i][j] < N:
            dp[i][j + graph[i][j]] += dp[i][j]

        # 아래쪽으로 이동
        if i + graph[i][j] < N:
            dp[i + graph[i][j]][j] += dp[i][j]