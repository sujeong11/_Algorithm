import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0 # 다시 방문하지 않도록
    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                count += 1

    return count


N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

count = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1: # 1일때만 방문
            count.append(bfs(graph, i, j))

count.sort()

print(len(count))
for c in count:
    print(c)