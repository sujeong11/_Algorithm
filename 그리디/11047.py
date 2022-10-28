N, K = map(int, input().split())

value = [int(input()) for _ in range(N)]
count = 0

for i in reversed(range(N)):
    count += (K // value[i])
    K = (K % value[i])

print(count)