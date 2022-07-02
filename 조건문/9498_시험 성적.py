# 언어: Python, (성공/실패) : 1/0, 메모리 : 30840KB, 시간 : 68ms

score = int(input())

if (89 < score <= 100):
    print('A')
elif (80 <= score < 90):
    print('B')
elif (70 <= score < 80):
    print('C')
elif (60 <= score < 70):
    print('D')
else:
    print('F')