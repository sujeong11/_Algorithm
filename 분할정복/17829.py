def pooling(elem, size):
    if size == 1:
        return elem[0][0]

    new_elem = [[] for _ in range(size // 2)]

    for i in range(0, size, 2):
        for j in range(0, size, 2):
            new_elem[i // 2].append(sorted([elem[i][j], elem[i][j + 1], elem[i + 1][j], elem[i + 1][j + 1]])[2])

    return pooling(new_elem, size // 2)

N = int(input())
elem = [list(map(int, input().split())) for _ in range(N)]
print(pooling(elem, N))