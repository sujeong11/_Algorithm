N, M = map(int, input().split())
cmd = [list(map(int, input().split())) for _ in range(M)]
seat = [[0] * 20 for _ in range(N)]
result = []

for i in range(len(cmd)):
    # 1번 명령
    if cmd[i][0] == 1:
        if seat[cmd[i][1]-1][cmd[i][2]-1] == 0:
            seat[cmd[i][1]-1][cmd[i][2]-1] = 1

    # 2번 명령
    if cmd[i][0] == 2:
        if seat[cmd[i][1] - 1][cmd[i][2] - 1] == 1:
            seat[cmd[i][1] - 1][cmd[i][2] - 1] = 0

    # 3번 명령
    if cmd[i][0] == 3:
        for j in range(19, 0, -1):
            seat[cmd[i][1]-1][j] = seat[cmd[i][1]-1][j-1]
        seat[cmd[i][1]-1][0] = 0

    # 4번 명령
    if cmd[i][0] == 4:
        for j in range(0, 19):
            seat[cmd[i][1]-1][j] = seat[cmd[i][1]-1][j+1]
        seat[cmd[i][1]-1][19] = 0

# 이전에 승객이 앉은 상태가 있었는지 체크
result.append(seat[0])
for i in seat:
    if i not in result:
        result.append(i)

print(len(result))