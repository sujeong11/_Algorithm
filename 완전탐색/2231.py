N = int(input())

for i in range(1, N+1):
    digits = list(map(int, str(i))) # 각 자리수를 리스트에 담는다.

    if i + sum(digits) == N:
        print(i)
        break

    if i == N:
        print(0)