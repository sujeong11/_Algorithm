# PyPy3로 해야 시간 초과가 발생하지 않음
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = [input().split() for _ in range(N)]

for _ in range(M):
    power = int(input())
    start, end = 0, len(data) - 1
    result = 0

    while start <= end:
        mid = (start + end) // 2

        if int(data[mid][1]) >= power:
            end = mid - 1
            result = mid
        else:
            start = mid + 1

    print(data[result][0])


# [ bisect 라이브러리 사용한 풀이 ]
# import sys
# import bisect
#
# input = sys.stdin.readline
# n, m = map(int, input().split())
# title = []
# power = [-1]
#
# for i in range(n):
#     t, p = map(str, input().rstrip().split())
#     title.append(t)
#     power.append(int(p))
#
# for _ in range(m):
#     p = int(input())
#     idx = bisect.bisect_left(power, p)
#     print(title[idx - 1])