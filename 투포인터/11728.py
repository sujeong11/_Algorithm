N, M = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = [0] * (N + M)
i = 0 # arr1을 가리키며 증가
j = 0 # arr2을 가리키며 증가
k = 0

while i < N or j < M:
    # arr2의 모든 원소가 처리되었거나, arr1의 원소가 더 작을 때
    if j >= M or (i < N and arr1[i] <= arr2[j]):
        result[k] = arr1[i]
        i += 1
    # arr1의 모든 원소가 처리되었거나, arr2의 원소가 더 작을 때
    else:
        result[k] = arr2[j]
        j += 1
    k += 1

print(*result)

# [ 풀이 2 ]
# N, M = map(int, input().split())
# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))
#
# comb_arr = arr1 + arr2
# comb_arr.sort()
#
# print(*comb_arr)