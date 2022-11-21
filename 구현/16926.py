# PyPy3로 언어 선택 시 맞힘

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for _ in range(R):
    for i in range(min(N, M) // 2):
        x, y = i, i
        val = arr[x][y]

        # 왼쪽 줄 이동
        for j in range(i + 1, N - i):
            x = j
            prev_val = arr[x][y]
            arr[x][y] = val
            val = prev_val

        # 아랫 줄 이동
        for j in range(i + 1, M - i):
            y = j
            prev_val = arr[x][y]
            arr[x][y] = val
            val = prev_val

        # 오른쪽 줄 이동
        for j in range(i + 1, N - i):
            x = N - j - 1
            prev_val = arr[x][y]
            arr[x][y] = val
            val = prev_val

        # 윗 줄 이동
        for j in range(i + 1, M - i):
            y = M - j - 1
            prev_val = arr[x][y]
            arr[x][y] = val
            val = prev_val

for i in arr:
    print(*i)