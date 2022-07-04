# 언어 : Python, (성공/실패) : 1/0, 메모리 : 30840KB, 시간 : 240ms

N = int(input())
nums = []

for i in range(N):
    nums.append(int(input()))

for i in range(len(nums)-1):
    for j in range(i, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

for i in nums:
    print(i)