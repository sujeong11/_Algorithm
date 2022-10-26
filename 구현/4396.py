N = int(input())

position = [list(input()) for _ in range(N)]
clicked = [list(input()) for _ in range(N)]
result = [['.'] * N for _ in range(N)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(N):
    for j in range(N):
        # 지뢰가 없으면서 열린 칸에는 0과 8 사이의 숫자가 있어야 한다.
        if position[i][j] == '.' and clicked[i][j] == 'x':
            count = 0

            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]

                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue

                if position[nx][ny] == '*':
                    count += 1

            result[i][j] = count

        # 지뢰가 있는 칸이 열렸다면 지뢰가 있는 모든 칸이 별표(*)로 표시
        if position[i][j] == '*' and clicked[i][j] == 'x':
            for x in range(N):
                for y in range(N):
                    if position[x][y] == '*':
                        result[x][y] = '*'

for i in range(N):
    for j in range(N):
        print(result[i][j], end='')
    print()