# 언어 : Python, (성공/실패) : 1/0, 메모리 : 30840KB, 시간 : 68ms

x = int(input())
y = int(input())

if (x > 0 and y > 0):
    print('1')
elif (x < 0 and y > 0):
    print('2')
elif (x < 0 and y < 0):
    print('3')
else:
    print('4')