from itertools import permutations

N = int(input())
num = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

for _ in range(N):
    req, strike, ball = map(int, input().split())
    req = list(str(req))
    remove_cnt = 0 # 배열에서 제거된 원소 개수

    for i in range(len(num)):
        strike_cnt, ball_cnt = 0, 0
        i -= remove_cnt

        for j in range(3):
            req[j] = int(req[j])

            if req[j] in num[i]:
                if j == num[i].index(req[j]):
                    strike_cnt += 1
                else:
                    ball_cnt += 1

        # 입력받은 값의 strike, ball 값과 count한 값이 맞지 않으면 배열에서 삭제
        if strike_cnt != strike or ball_cnt != ball:
            num.remove(num[i])
            remove_cnt += 1

print(len(num))