H, W = map(int, input().split())
N = int(input())
sticker = [list(map(int, input().split())) for _ in range(N)]
result = 0

for i in range(N):
    for j in range(i+1, N):
        row1, col1 = sticker[i]
        row2, col2 = sticker[j]

        # 스티커 2개 모두 90도 회전하지 않을 경우
        if (row1 + row2 <= H and max(col1, col2) <= W) or (max(row1, row2) <= H and col1 + col2 <= W):
            result = max(result, (row1 * col1) + row2 * col2)
        # 첫 번쨰 스티커만 90도 회전할 경우
        if (col1 + row2 <= H and max(row1, col2) <= W) or (max(col1, row2) <= H and row1 + col2 <= W):
            result = max(result, row1 * col1 + row2 * col2)
        # 두 번쨰 스티커만 90도 회전할 경우
        if (row1 + col2 <= H and max(col1, row2) <= W) or (max(row1, col2) <= H and col1 + row2 <= W):
            result = max(result, row1 * col1 + row2 * col2)
        # 스티커 2개 모두 90도 회전할 경우
        if (col1 + col2 <= H and max(row1, row2) <= W) or (max(col1, col2) <= H and row1 + row2 <= W):
            result = max(result, row1 * col1 + row2 * col2)

print(result)