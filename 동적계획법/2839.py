N = int(input())
count = 0

while N >= 0:
    # IDEA: 5의 배수가 될 때까지 3을 빼주고 봉지 개수 출력
    if N % 5 == 0:
        count += (N // 5)
        print(count)
        break
    N -= 3
    count += 1
else: # while문이 거짓일 경우
    print(-1)