def quad(x, y, size):
    p = graph[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if p != graph[i][j]:
                p = -1
                break

    if p == -1:
        print("(", end='')
        size = size // 2
        quad(x, y, size)
        quad(x, y + size, size)
        quad(x + size, y, size)
        quad(x + size, y + size, size)
        print(")", end='')
    elif p == 1:
        print(1, end='')
    else:
        print(0, end='')


N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
quad(0, 0, N)