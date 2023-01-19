import sys
input = sys.stdin.readline

N, M = map(int, input().split())
L = sorted(list(map(int, input().split())))
result = []

def back_tracking(start):
    if len(result) == M:
        print(" ".join(map(str, result)))
        return
    for i in range(N):
        if L[i] not in result:
            result.append(L[i])
            back_tracking(start + 1)
            result.pop()

back_tracking(0)