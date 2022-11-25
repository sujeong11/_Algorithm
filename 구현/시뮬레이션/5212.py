import copy

R, C = map(int, input().split())
cur_map = [list(input()) for _ in range(R)]
result = copy.deepcopy(cur_map)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(R):
    for j in range(C):
        if cur_map[i][j] == 'X':
            count = 0

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if nx < 0 or ny < 0 or nx >= R or ny >= C:
                    count += 1 # 지도의 범위를 벗어나는 칸은 모두 바다이므로
                elif cur_map[nx][ny] == '.':
                    count += 1

            if count >= 3:
                result[i][j] = '.'

# 모든 섬을 포함하는 가장 작은 직사각형으로 지도의 크기 만들기
row = []
col = []

for i in range(R):
    for j in range(C):
        if result[i][j] == 'X':
            row.append(i)
            col.append(j)

if row:
    for i in range(min(row), max(row) + 1):
        for j in range(min(col), max(col) + 1):
            print(result[i][j], end='')
        print()
else: # 섬은 적어도 1개는 있으므로
    print('X')