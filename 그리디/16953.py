A, B = map(int, input().split())
count = 1

while True: # B -> A가 되도록
    if A == B:
        break
    elif A > B: # 만들 수 없는 경우
        count = -1
        break

    if B % 10 == 1:
        B //= 10
        count += 1
    elif B % 2 == 0:
        B //= 2
        count += 1
    else: # 만들 수 없는 경우
        count = -1
        break

print(count)