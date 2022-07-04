# 언어: Python, (성공/실패) : 1/1, 메모리 : 30840KB, 시간 : 1500ms

N = int(input())
result = 0

for i in range(1, N+1):
    nums = list(map(int, str(i)))
    result = i + sum(nums)

    if (result == N):
        print(i)
        break

    if (i == N):
        print('0')



