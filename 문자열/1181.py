N = int(input())
word = [input() for _ in range(N)]
word = list(set(word))

word.sort() # 오름차순 정렬
word.sort(key=lambda x: len(x)) # 길이가 짧은 순서대로 정렬

for i in range(len(word)):
    print(word[i])