import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

N, M, K, X = map(int, input().split())
graph = [[] for i in range(N + 1)]
distance = [INF] * (N + 1) # 최단 거리 테이블
result = []

# 모든 간선 정보를 입력받기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(X)

for i in range(1, N + 1):
    if distance[i] == K:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    for i in result:
        print(i)