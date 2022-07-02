# 언어: Python, (성공/실패) : 1/0, 메모리 : 30840KB, 시간 : 72ms

A = int(input())
B = int(input())
C = int(input())

cal = str(A * B * C)

for i in range(10):
    print(cal.count('{}'.format(i)))

