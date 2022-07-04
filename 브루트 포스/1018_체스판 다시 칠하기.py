# 언어 : Python, (성공/실패) : 1/2, 메모리 : 30840KB, 시간 : 116ms

N, M = map(int, input().split())
board = []
count = []

for _ in range(N):
    board.append(input())

# 첫 번째, 두 번쨰 for문은 원래의 체스 판에서 8*8로 자를 수 있는 범위의 시작점 (여러 개 존재)
for a in range(N-7):
    for b in range(M-7):
        idx1 = 0 # 'W'로 시작할 경우 바뀐 체스 판의 갯수를 세기 위한 것
        idx2 = 0 # 'B'로 시작할 경우 바뀐 체스 판의 갯수를 세기 위한 것

        # 자른 체스의 시작점을 기준으로 8칸을 모두 체크
        # i는 행의 번호, j는 열의 번호
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    # 합이 짝수 일 경우 시작점의 색깔과 같아야 한다.
                    if board[i][j] != 'W':
                        idx1 += 1
                    if board[i][j] != 'B':
                        idx2 += 1
                else:
                    if board[i][j] != 'B':
                        idx1 += 1
                    if board[i][j] != 'W':
                        idx2 += 1
        count.append(min(idx1, idx2))

print(min(count))