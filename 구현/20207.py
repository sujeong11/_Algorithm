calendar = [0] * 366
row, col, result = 0, 0, 0

N = int(input())
for _ in range(N):
    S, E = map(int, input().split())

    for i in range(S, E+1):
        calendar[i] += 1

for i in range(366):
    if calendar[i] != 0:
        row = max(row, calendar[i])
        col += 1
    else:
        result += (row * col)
        row = 0
        col = 0

result += (row * col)
print(result)