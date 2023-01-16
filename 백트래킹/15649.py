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
        if i not in result: # 중복 확인
            result.append(i)
            back_tracking() # 재귀
            result.pop() # 다음 수로 넘어가도록

back_tracking()