N = int(input())
times = list(map(int, input().split()))
result = 0

times.sort(reverse=True)

for i in range(len(times)):
    for j in range(i, len(times)):
        result += times[j]

print(result)