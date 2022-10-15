# 언어 : Python, (성공/실패) : 1/1, 메모리 : 30840KB, 시간 : 68ms

N = int(input())
reverse = []

for i in str(N):
    reverse.append(int(i))

reverse.sort(reverse=True)

for i in reverse:
    print(i, end='')