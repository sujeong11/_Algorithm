# 언어 : Python, (성공/실패) : 1/1, 메모리 : 51616KB, 시간 : 4240ms

N = int(input())
coord = []

for i in range(N):
    x, y = map(int, input().split())
    coord.append((x, y))

coord.sort(key= lambda x: (x[0], x[1]))

for i in coord:
    print(i[0], i[1])
