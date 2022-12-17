import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    score = []
    for _ in range(2):
        score.append(list(map(int, input().split())))

    for j in range(1, n):
        if j == 1: # 왼쪽 대각선을 더한다.
            score[0][j] += score[1][j - 1]
            score[1][j] += score[0][j - 1]
        else: # 왼쪽 대각선이나 이 값의 왼쪽 값을 더할 수 있다.
            score[0][j] += max(score[1][j - 1], score[1][j - 2])
            score[1][j] += max(score[0][j - 1], score[0][j - 2])

    print(max(score[0][n - 1], score[1][n - 1]))