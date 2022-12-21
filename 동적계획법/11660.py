import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (N + 1) for _ in range(N + 1)] # 누적합 사용을 위해 (행/열 + 1)을 한 크기로 초기화

# 2차원 누적합 이용 (1행, 1열은 사용하지 않음)
for i in range(N):
    for j in range(N):
        dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j] - dp[i][j]) + graph[i][j] # 겹치는 부분은 빼줘야 한다.

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - (dp[x1 - 1][y2] + dp[x2][y1 - 1] - dp[x1 - 1][y1 - 1])) # x2와 y2의 최종합에서 필요없는 부분을 제거해준다.