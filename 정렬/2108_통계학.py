# 언어 : Python, (성공/실패) : 1/1, 메모리 : 56100KB, 시간 : 508ms

import sys
from collections import Counter

N = int(sys.stdin.readline())
nums = []

for i in range(N):
    nums.append(int(sys.stdin.readline()))

nums = sorted(nums)

#산술평균
print(round(sum(nums) / N))

# 중앙값
print(nums[int(len(nums) / 2)])

# 최빈값
counter = Counter(nums).most_common()
if len(counter) > 1:
    if counter[0][1] == counter[1][1]:
        print(counter[1][0])
    else:
        print(counter[0][0])
else:
    print(counter[0][0])

# 범위
print(nums[-1]-nums[0]) # print(nums[len(nums)-1] - nums[0])