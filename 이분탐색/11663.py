import bisect
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dot = sorted(list(map(int, input().split()))) # 이진 탐색을 위해 정렬

for _ in range(M):
    x, y = map(int, input().split())
    x_idx = bisect.bisect_left(dot, x)
    y_idx = bisect.bisect_right(dot, y)
    print(y_idx - x_idx)