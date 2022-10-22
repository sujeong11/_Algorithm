N = int(input())
tip = []
count = 1
result = 0

for i in range(N):
    tip.append(int(input()))

tip.sort(reverse=True)

for i in range(len(tip)):
    tip[i] = tip[i] - ((i+1) - 1)
    if (tip[i] < 0):
        tip[i] = 0
    result += tip[i]

print(result)