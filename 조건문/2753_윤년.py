# 언어: Python, (성공/실패) : 1/0, 메모리 : 30840KB, 시간 : 72ms

year = int(input())

if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    print('1')
else:
    print('0')
