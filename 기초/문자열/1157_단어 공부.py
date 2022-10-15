# 언어 : Python, (성공/실패) : 1/1, 메모리 : 32796KB, 시간 : 104ms

word = input().upper()
unique_word = list(set(word)) # 중복 값을 제거한 단어
cnt_list = []

for i in unique_word:
    cnt = word.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    print(unique_word[(cnt_list.index(max(cnt_list)))])