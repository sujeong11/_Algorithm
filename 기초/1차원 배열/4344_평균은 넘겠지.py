# 언어 : Python, (성공/실패) : 1/1, 메모리 : 30840KB, 시간 : 72ms

C = int(input())

for i in range(C):
    N = list(map(int, input().split()))
    avg = sum(N[1:]) / N[0]
    count = 0

    for i in N[1:]:
        if (avg < i):
            count += 1

    print("{:.3f}%".format((count / N[0]) * 100))

