money = int(input())
stock = list(map(int, input().split()))

money_j, money_s = money, money
count_j, count_s = 0, 0

for i in stock:
    while money_j >= i:
        money_j -= i
        count_j += 1

for i in range(11):
    if (stock[i] > stock[i+1] > stock[i+2]):
        while money_s >= stock[i + 3]:
            money_s -= stock[i + 3]
            count_s += 1
    if (stock[i] < stock[i + 1] < stock[i + 2]):
        while count_s > 0:
            money_s += stock[i + 3]
            count_s -= 1

result_j = money_j + (stock[-1] * count_j)
result_s = money_s + (stock[-1] * count_s)

if result_j > result_s:
    print("BNP")
elif result_j < result_s:
    print("TIMING")
else:
    print("SAMESAME")
