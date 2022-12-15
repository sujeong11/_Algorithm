import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

# 이전까지 모든 숫자의 합 중 최대값을 기록하며 계산
for i in range(1, n):
    nums[i] = max(nums[i], nums[i-1] + nums[i])

print(max(nums))