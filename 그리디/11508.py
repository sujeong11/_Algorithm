N = int(input())

costs = [int(input()) for _ in range(N)]
split_cost = []
result = 0

# 제품이 3개가 아닐 때 최소값을 가져야하므로
costs.sort(reverse=True)

for i in range(0, len(costs), 3):
    split_cost.append(costs[i:i+3])

for i in range(len(split_cost)):
    if len(split_cost[i]) == 1:
        result += split_cost[i][0]
    else:
        result += (split_cost[i][0] + split_cost[i][1])

print(result)