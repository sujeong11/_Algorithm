import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))
left, right, result = 0, 0, 0
counter = [0] * (max(nums) + 1)

while right < N:
    if counter[nums[right]] < K: # 같은 원소가 K개 이하라면 right로 계속 이동
        counter[nums[right]] += 1
        right += 1
    else: # 같은 원소가 K개 이상이라면 같은 원소가 K개 이하가 될 때까지 left를 계속 이동
        counter[nums[left]] -= 1
        left += 1
    result = max(result, right - left)

print(result)