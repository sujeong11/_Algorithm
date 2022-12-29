N, M = map(int, input().split())
listen = {input() for _ in range(N)}
see = {input() for _ in range(M)}

result = sorted(list(listen & see))

print(len(result))

for i in range(len(result)):
    print(result[i])