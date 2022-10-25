N = int(input())
count = 0
status = dict()

for i in range(N):
    num, position = map(int, input().split())

    if num not in status: # 딕셔너리에 없는 값이였다면 그냥 넣는다.
        status[num] = position
    else: # 딕셔너리에 있던 값이면 위치가 바뀌였는지 확인해 값을 업데이트
        if (status[num] != position):
            count += 1
            status[num] = position

print(count)