# 언어 : Python, (성공/실패) : 1/1, 메모리 : 30840KB, 시간 : 68ms

H, M = map(int, input().split())

if (M >= 45):
    print(H, M - 45)
elif (H > 0 and M < 45):
    print(H - 1, M + 15)
elif (H == 0 and M < 45): # 자정일 때
    print(23, M + 15)