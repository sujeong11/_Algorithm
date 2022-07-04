# 언어 : Python, (성공/실패) : 1/1, 메모리 : 30840KB, 시간 : 76ms

N = int(input())
info = []

for i in range(N):
    x, y = map(int, input().split())
    info.append((x, y))

for i in info:
    rank = 1
    for j in info: # 전체를 다 검색
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')