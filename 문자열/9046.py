T = int(input())

for _ in range(T):
    str = input().replace(' ', '')
    count_str = [0] * 26 # 알파벳 횟수를 체크하기 위한 변수

    for i in str:
        count_str[ord(i) - 97] += 1

    if count_str.count(max(count_str)) > 1:
        print('?')
    else:
        print(chr(97 + count_str.index(max(count_str))))