import sys
# from collections import deque
sys.setrecursionlimit(10**9) # 기본으로 반복은 1000회로 제한되어 있기 떄문에 늘려줘야 한다.
input = sys.stdin.readline


def dfs(graph, start, visited):
    for i in graph[start]:
        # DFS는 항상 부모에서 자식으로 이동한다는 점 활용
        if visited[i] == 0:
            visited[i] = start
            dfs(graph, i, visited)

# def bfs(graph, start, visited):
#     queue = deque([start])
#     while queue:
#         v = queue.popleft()
#         for i in graph[v]:
#             if visited[i] == 0:
#                 queue.append(i)
#                 visited[i] = v

N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

# 인접리스트
for _ in range(N - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(graph, 1, visited)
# bfs(graph, 1, visited)

# 부모 노드는 2번째 노드부터 출력
for i in range(2, N + 1):
    print(visited[i])