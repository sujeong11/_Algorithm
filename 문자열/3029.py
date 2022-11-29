h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
result = 0

# 연산을 위해 초로 변환
cur_time = h1 * 3600 + m1 * 60 + s1
throw_time = h2 * 3600 + m2 * 60 + s2

if (cur_time >= throw_time): # 정각을 넘어가는 경우
    result = throw_time - cur_time + (24 * 3600) # 24시간을 더해준다.
else:
    result = throw_time - cur_time

hour = result // 60 // 60
min = result // 60 % 60
sec = result % 60

print("%02d:%02d:%02d" % (hour, min, sec))