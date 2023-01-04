def solution(x, y, size):
    global count

    if x > r or x + size <= r or y > c or y + size <= c:
        count += (size ** 2)
        return

    if size > 2:
        size //= 2
        solution(x, y, size)
        solution(x, y + size, size)
        solution(x + size, y, size)
        solution(x + size, y + size, size)
    else:
        if x == r and y == c:
            print(count)
        elif x == r and y + 1 == c:
            print(count + 1)
        elif x + 1 == r and y == c:
            print(count + 2)
        else:
            print(count + 3)
        return

N, r, c = map(int, input().split())
count = 0
solution(0, 0, 2 ** N)