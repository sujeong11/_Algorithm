import sys
input = sys.stdin.readline

text = [input().strip() for _ in range(5)]

for i in range(max(len(k) for k in text)):
    for j in range(5):
        if i < len(text[j]):
            print(text[j][i], end='')