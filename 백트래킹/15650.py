import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = []

def back_tracking(start):
    if len(result) == M:
        print(" ".join(map(str, result)))
        return
    for i in range(start, N + 1):
        if i not in result:
            result.append(i)
            back_tracking(i + 1) # 앞의 숫자가 뒤의 숫자보다 큰 경우 제외하도록
            result.pop()

back_tracking(1)