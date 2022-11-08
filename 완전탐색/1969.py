N, M = map(int, input().split())
DNA = [input() for _ in range(N)]
result = ''
hd = 0

for i in range(M):
    a, c, g, t = 0, 0, 0, 0

    for j in range(N):
        if DNA[j][i] == 'A':
            a += 1
        elif DNA[j][i] == 'C':
            c += 1
        elif DNA[j][i] == 'G':
            g += 1
        elif DNA[j][i] == 'T':
            t += 1

    max_DNA = max(a, c, g, t)
    hd += (N - max_DNA)

    if max_DNA == a:
        result += "A"
    elif max_DNA == c:
        result += "C"
    elif max_DNA == g:
        result += "G"
    elif max_DNA == t:
        result += "T"

print(result)
print(hd)