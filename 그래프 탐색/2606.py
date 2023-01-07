N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

# 인접리스트
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(graph, start, visited):
    visited[start] = 1
    # 연결된 부분 방문
    for i in graph[start]:
        if visited[i] == 0:
            dfs(graph, i, visited)

dfs(graph, 1, visited)
print(sum(visited) - 1) # 1번 컴퓨터빼고 출력