N, M = map(int, input().split())
status = list(map(int, input().split()))
commands = [list(map(int, input().split())) for _ in range(M)]

for cmd in commands:
    if cmd[0] == 1:
        status[cmd[1]-1] = cmd[2]
    elif cmd[0] == 2:
        for i in range(cmd[1]-1, cmd[2]):
            if status[i] == 1:
                status[i] = 0
            else:
                status[i] = 1
    elif cmd[0] == 3:
        for i in range(cmd[1]-1, cmd[2]):
            status[i] = 0
    else:
        for i in range(cmd[1]-1, cmd[2]):
            status[i] = 1

print(*status)