# 백트레킹으로 풀이할 시 시간 초과 발생
n = int(input())
nums = list(map(int, input().split()))

prefix_sum = 0
sum = 0

# 1 * -2
# (1 + (-2)) * 3
for i in range(n-1):
    prefix_sum += nums[i]
    sum += nums[i+1] * prefix_sum

print(sum)