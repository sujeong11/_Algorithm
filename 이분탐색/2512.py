N = int(input())
budget = list(map(int, input().split()))
M = int(input())
start, end = 0, max(budget)

while start <= end:
    mid = (start + end) // 2
    total = 0 # 배정된 총 예산

    for i in budget:
        if i >= mid:
            total += mid
        else:
            total += i

    if total <= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)