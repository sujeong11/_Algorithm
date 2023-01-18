import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = []

def back_tracking(start):
    if len(result) == M:
        print(" ".join(map(str, result)))
        return
    for i in range(start, N + 1):
        result.append(i)
        back_tracking(i)  # 비내림차순
        result.pop()

back_tracking(1)