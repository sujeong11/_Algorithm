import sys
input = sys.stdin.readline

def solution(x, y, N):
    global white, blue
    color = graph[x][y]

    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != graph[i][j]:
                solution(x, y, N // 2)
                solution(x, y + N // 2, N // 2)
                solution(x + N // 2, y, N // 2)
                solution(x + N // 2, y + N // 2, N // 2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0

solution(0, 0, N)

print(white)
print(blue)