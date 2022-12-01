from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
member_idx = list(i for i in range(N))
result = 1e9

for i in range(1, int(N//2) + 1):
    member_divide = combinations(S, i)

    for x in member_divide:
        start_list = list(x)
        link_list = list(member_idx - start_list)

        start_sum = 0
        link_sum = 0
        for j in range(N-1):
            for 

