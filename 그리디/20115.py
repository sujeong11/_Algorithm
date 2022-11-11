N = int(input())
volume = list(map(int, input().split()))

volume.sort(reverse=True)
result = volume[0]

for i in range(1, N):
    result += volume[i] / 2

print("%g" %result) # 의미없는 소수점 제거를 위해