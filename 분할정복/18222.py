# 투에-모스 수열 점화식 이용
def recursive(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if x % 2:
        return 1 - recursive(x // 2)
    else:
        return recursive(x // 2)

k = int(input())
print(recursive(k - 1))