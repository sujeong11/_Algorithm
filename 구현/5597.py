student = [False] * 30

for i in range(28):
    num = int(input())
    student[num - 1] = True

for i in range(30):
    if student[i] == False:
        print(i + 1)