# 언어: Python, (성공/실패) : 1/1, 메모리 : 30840KB, 시간 : 72ms

S = input()
alphabet = list(range(97, 123))

for i in alphabet:
    print(S.find(chr(i)))