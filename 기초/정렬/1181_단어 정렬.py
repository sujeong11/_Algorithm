# 언어 : Python, (성공/실패) : 1/1, 메모리 : 35452KB, 시간 : 104ms

import sys

N = int(input())
words = []

for i in range(N):
    words.append(sys.stdin.readline().strip()) #'\n'제거 해야 한다.

words = set(words)
words = list(words)

words.sort() # 먼저, 알파벳 순서부터 정렬
words.sort(key= len)

for i in words:
    print(i)