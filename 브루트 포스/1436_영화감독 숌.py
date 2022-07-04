# 언어: Python, (성공/실패) : 1/1, 메모리 : 30840KB, 시간 : 860ms

N = int(input())
num = 666
cnt = 0

while True:
    if ('666' in str(num)):
        cnt += 1

    if cnt == N:
        print(num)
        break

    num += 1