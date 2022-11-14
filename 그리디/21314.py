# 최대값 - 10 ^ (K가 나오기 전의 M의 개수) * 5
# 최소값 - 10 ^ (K가 나오기 전의 M의 개수) + 5

string = input().rstrip()

m = 0
max = ''
min = ''

for i in string:
    if i == 'M':
        m += 1
    else:
        if m > 0:
            max += str((10 ** m) * 5)
            min += str((10 ** m) + 5)
        else:
            max += '5'
            min += '5'
        m = 0

# 'M'으로 끝날 경우
if m > 0:
    max += '1' * m
    min += str(10 ** (m-1))

print(max)
print(min)