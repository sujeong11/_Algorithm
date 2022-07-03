# 언어: Python, (성공/실패) : 1/1, 메모리 : 30840KB, 시간 : 80ms

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
cnt = 0

for i in word:
    for j in range(len(dial)):
        if i in dial[j]:
            cnt += (dial.index(dial[j]) + 2)
            break

print(cnt + len(word))