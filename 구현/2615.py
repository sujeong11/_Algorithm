n = 19
board = [list(map(int, input().split())) for _ in range(n)]

# → ↓ ↘ ↗
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

# 전체 오목판을 0이 아니면 → ↓ ↘ ↗ 방향으로 탐색해서 누가 오목을 완성했는지 판단한다.
for x in range(n):
    for y in range(n):
        if board[x][y] != 0:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                count = 1

                while 0 <= nx < n and 0 <= ny < n and board[nx][ny] == board[x][y]:
                    count += 1

                    if count == 5:
                        # 육목인지 체크한다.
                        if 0 <= x - dx[i] < n and 0 <= y - dy[i] < n and board[x - dx[i]][y - dy[i]] == board[x][y]:
                            break
                        if 0 <= nx + dx[i] < n and 0 <= ny + dy[i] < n and board[nx + dx[i]][ny + dy[i]] == board[x][y]:
                            break
                        print(board[x][y])
                        print(x + 1, y + 1)
                        exit(0)

                    nx += dx[i]
                    ny += dy[i]

print(0)