# 내장함수 permutations으로 풀이 가능
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = []

def back_tracking():
    if len(result) == M:
        print(" ".join(map(str, result)))
        return
    for i in range(1, N + 1):
        if i not in result:
            result.append(i)
            back_tracking() # 재귀
            result.pop()

back_tracking()