def plus_turn45(n, count, arr):
    n = n - 1

    for _ in range(count):
        prev_arr = []

        for i in range(n + 1):  # 주 대각선
            prev_arr.append(arr[i][i])

        for i in range(n + 1):  # 주 대각선 -> 가운데 열
            temp = arr[i][(n + 1) // 2]
            arr[i][(n + 1) // 2] = prev_arr[i]
            prev_arr[i] = temp

        for i in range(n + 1):  # 가운데 열 -> 부 대각선
            temp = arr[i][n - i]
            arr[i][n - i] = prev_arr[i]
            prev_arr[i] = temp

        for i in range(n + 1):  # 부 대각선 -> 가운데 행
            temp = arr[(n + 1) // 2][n - i]
            arr[(n + 1) // 2][n - i] = prev_arr[i]
            prev_arr[i] = temp

        for i in range(n + 1):  # 가운데 행 -> 주 대각선
            arr[n - i][n - i] = prev_arr[i]

def minus_turn45(n, count, arr):
    n = n - 1

    for _ in range(count):
        prev_arr = list()

        for i in range(n + 1):  # 주 대각선
            prev_arr.append(arr[i][i])

        for i in range(n + 1):  # 주 대각선 -> 가운데 행
            temp = arr[(n + 1) // 2][i]
            arr[(n + 1) // 2][i] = prev_arr[i]
            prev_arr[i] = temp

        for i in range(n + 1):  # 가운데 행 -> 부 대각선
            temp = arr[n - i][i]
            arr[n - i][i] = prev_arr[i]
            prev_arr[i] = temp

        for i in range(n + 1):  # 부 대각선 -> 가운데 열
            temp = arr[n - i][(n + 1) // 2]
            arr[n - i][(n + 1) // 2] = prev_arr[i]
            prev_arr[i] = temp

        for i in range(n + 1):  # 가운대 열 -> 주 대각선
            arr[n - i][n - i] = prev_arr[i]


# 값 입력받고 함수 실행해 결과 출력
T = int(input())

for _ in range(T):
    n, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    count = abs(d) // 45

    if d >= 0:
        plus_turn45(n, count, arr)
    else:
        minus_turn45(n, count, arr)

    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()