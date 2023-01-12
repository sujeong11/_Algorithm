import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while distance:
        x, y = distance.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == 1:
                distance.append((nx, ny))
                visited[nx][ny] = True
                result[nx][ny] = result[x][y] + 1


N, M = map(int, input().split())
graph = []
distance = deque([])
visited = [[False] * M for _ in range(N)]
result = [[-1] * M for _ in range(N)]

for i in range(N):
    row = list(map(int, input().split()))

    # 목표지점 표시
    for j in range(M):
        if row[j] == 2:
            distance.append((i, j))
            visited[i][j] = True
            row[j] = 0 # 자기 자신으로 가는 거리

        # 갈 수 없는 땅 표시
        if row[j] == 0:
            result[i][j] = 0

    graph.append(row)

# 거리 탐색
bfs()

for row in result:
    print(*row)