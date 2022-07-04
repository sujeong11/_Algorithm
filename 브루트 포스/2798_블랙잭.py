# 언어: Python, (성공/실패) : 1/0, 메모리 : 30840KB, 시간 : 132ms

N, M = map(int, input().split())
nums = list(map(int, input().split()))
max_val = 0

for i in range(len(nums)-2):
    for j in range(i+1, len(nums)-1):
        for k in range(j+1, len(nums)):
            if (nums[i] + nums[j] + nums[k] > M):
                continue # break로 하면 for문 자체를 빠져나가므로
            if (nums[i] + nums[j] + nums[k] > max_val):
                max_val = nums[i] + nums[j] + nums[k]

print(max_val)


