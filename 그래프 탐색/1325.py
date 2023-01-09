# PyPy3로 재출
import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, start):
    count = 1 # 방문한 정점의 개수
    queue = deque([start])
    visited = [0] * (N + 1)
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1

    return count

N, M = map(int,input().split())
graph = [[] for _ in range(N + 1)]
max_count = 1
result = []

for _ in range(M):
    x, y = map(int, input().split())
    graph[y].append(x) # A가 B를 신뢰 -> 단방향

for i in range(1, N + 1):
    count = bfs(graph, i)

    if count > max_count:
        max_count = count
        result.clear()
        result.append(i)
    elif count == max_count:
        result.append(i)

print(*result)