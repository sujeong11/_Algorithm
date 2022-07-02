# 언어: Python, (성공/실패) : 1/0, 메모리 : 30840KB, 시간 : 68ms

x = int(input())
y = int(input())

num = []

for i in str(y):
    num.append(int(i))

for i in range(len(str(y)) - 1, -1, -1):
    print(x * num[i])

print(x * y)
