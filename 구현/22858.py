N, K = map(int, input().split())
S = list(map(int, input().split()))
D = list(map(int, input().split()))

for _ in range(K):
    result = [0] * N # 한 번 섞을 때마다 리셋

    for i in range(N):
        result[D[i]-1] = S[i]
    # 값 누적을 위해, 한 번 섞은 전의 카드 S로 이동
    S = result

print(*S)