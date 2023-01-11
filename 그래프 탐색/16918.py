import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while bomb:
        x, y = bomb.popleft()
        graph[x][y] = '.'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == 'O':
                graph[nx][ny] = '.'

def save_bomb():
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 'O':
                bomb.append((i, j))

R, C, N = map(int, input().split())
graph = [list(map(str, input().rstrip())) for _ in range(R)] # 1단계: 폭발 설치
bomb = deque()

# 2단계: 봄버맨은 아무것도 하지 않음(1부터 시작) -> 3, 4단계 반복
for time in range(1, N + 1):
    if time == 1:
        save_bomb()
    elif time % 2 == 1:
        # 4단계: 3초전 설치된 폭탄 폭발
        bfs()
        save_bomb()
    else:
        # 3단계: 모든 칸에 폭발 설치
        graph = [['O'] * C for _r in range(R)]

for i in graph:
    print("".join(i))