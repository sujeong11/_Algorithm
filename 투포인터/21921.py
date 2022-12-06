import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visitor = list(map(int, input().split()))

if max(visitor) == 0:
    print("SAD")
else:
    val = sum(visitor[:X])

    max_val = val
    max_cnt = 1

    for i in range(X, N):
        val += visitor[i]
        val -= visitor[i-X]

        if val > max_val: # 새로운 최대값 찾았을 때
            max_val = val
            max_cnt = 1
        elif val == max_val: # 최대값과 같은 값을 찾았을 때
            max_cnt += 1

    print(max_val)
    print(max_cnt)