N = int(input())
loss = list(map(int, input().split()))

loss.sort()
temp = []

if (N % 2 == 1): # 홀수 일 때는 가장 큰 값이 혼자 선택되도록
    temp.append(loss[-1])
    loss = loss[:-1]

for i in range(len(loss) // 2):
    # 가장 작은 값과 가장 큰 값을 더해줘야 결과 값이 가장 작아지므로
    temp.append(loss[i] + loss[len(loss) - i - 1])

print(max(temp))