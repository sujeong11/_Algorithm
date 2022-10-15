N = int(input())

def hanoi(n, a, b, c): # 원반 개수, 시작, 보조, 목표
    if n == 1:
        print(a, c) # 바로 목표로
    else:
        hanoi(n - 1, a, c, b) # 더 작은 것을 보조 위치로 이동
        print(a, c) # 다음으로 작은 것은 바로 목표 위치로 이동
        hanoi(n - 1, b, a, c) # 더 작은 것을 목표 위치로 이동

sum = 1

for i in range(N - 1):
    sum = sum * 2 + 1

print(sum)

hanoi(N, 1, 2, 3)