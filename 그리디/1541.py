# -가 나오기 전까지 더해줘야 최소 값이 나오므로
exp = input().split('-')
result = 0

for i in exp[0].split('+'): # +만 있을 때를 고려해야 하므로
    result += int(i)

for i in exp[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)