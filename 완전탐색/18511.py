from itertools import product # 중복 순열 (순서 o, 중복 o)


N, K = map(int, input().split())
elem = list(map(str, input().split()))
length = len(str(N))

while True:
    temp = list(product(elem, repeat=length))
    result = []

    for i in temp:
        if int("".join(i)) <= N:
            result.append(int("".join(i)))

    if len(result) >= 1:
        print(max(result))
        break
    else:
        length -= 1