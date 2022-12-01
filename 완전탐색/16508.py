T = input()
N = int(input())
price, name = [], []
for _ in range(N):
    temp = map(str, input().split())
    price.append(int(temp[0]))
    name.append(temp[1])