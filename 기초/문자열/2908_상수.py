# 언어 : Python, (성공/실패) : 1/0, 메모리 : 30840KB, 시간 : 68ms

A, B = map(str, input().split())
A = int(A[::-1])
B = int(B[::-1])

if (A > B):
    print(A)
else:
    print(B)