N, K = map(int, input().split())

values = [int(input()) for _ in range(N)]
count = 0

for i in reversed(range(N)):
    count += (K // values[i])
    K = (K % values[i])

print(count)