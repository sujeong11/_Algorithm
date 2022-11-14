N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]

# 1. 회의가 끝나는 시간의 오름차순 (빨리 끝낼수록 뒤에서 고려할 회의 수가 많아지기 때문)
# 2. 시작하는 시간의 오름차순
times.sort(key = lambda x: (x[1], x[0]))
count = 1
end_time = times[0][1]

for i in range(1, N):
    if times[i][0] >= end_time:
        count += 1
        end_time = times[i][1]

print(count)