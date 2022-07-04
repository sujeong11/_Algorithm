# 언어 : Python, (성공/실패) : 1/1, 메모리 : 30840KB, 시간 : 72ms

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for i in croatia:
    word = word.replace(i, "!")

print(len(word))