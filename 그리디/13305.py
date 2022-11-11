N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0] # 가격이 가장 싼 기름을 이용하기 위해
result = 0

for i in range(N-1):
    if price[i] < min_price:
        min_price = price[i]
    result += (distance[i] * min_price)

print(result)