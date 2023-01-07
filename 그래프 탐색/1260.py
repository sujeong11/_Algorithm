from collections import deque

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited_dfs = [0] * (N+1)
visited_bfs = [0] * (N+1)

# 인접리스트
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 정점 번호가 작은 것 먼저 방문할 수 있도록 정렬
for row in graph:
    row.sort()

dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)